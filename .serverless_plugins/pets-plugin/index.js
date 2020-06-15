'use strict';
const util = require('util');
const AWS = require('aws-sdk');
const request = require('request-promise');

class ServerlessPlugin {

  constructor(serverless, options) {
    this.serverless = serverless;
    this.options = options;
    this.provider = this.serverless.getProvider('aws');

    this.commands = {
      pets: {
        usage: 'A plugin for the Pets API.',
        commands: {
          seed: {
            usage: 'Seed some sample data into DynamoDB.',
            lifecycleEvents: ['seed']
          },
          list: {
            usage: 'List pets in DynamoDB.',
            lifecycleEvents: ['list']
          }
        }
      }
    };

    this.hooks = {
      'pets:seed:seed': this.seed.bind(this),
      'pets:list:list': this.list.bind(this)
    };
  }

  async seed() {

    // Get Seed Data from S3
    this.serverless.cli.log("Starting seeding process...");
    const s3 = new AWS.S3();
    const bucketName = util.format('%s-%s',
      this.serverless.service.getServiceName(),
      this.provider.getStage()
    );
    const endpoint = await this.getEndpoint();

    this.serverless.cli.log("Adding Durant...");
    let r = await this.provider.request('S3', 'getObject', {
      Bucket: bucketName,
      Key: 'durant.json'
    });
    await request({
      url: `${endpoint}/pets`,
      method: 'POST',
      json: JSON.parse(r.Body.toString('utf-8'))
    });

    this.serverless.cli.log("Adding Penny...");
    r = await this.provider.request('S3', 'getObject', {
      Bucket: bucketName,
      Key: 'penny.json'
    });
    await request({
      url: `${endpoint}/pets`,
      method: 'POST',
      json: JSON.parse(r.Body.toString('utf-8'))
    });

  }

  async list() {
    this.serverless.cli.log("Listing Pets...");
    const endpoint = await this.getEndpoint();
    const r = await request({
      url: `${endpoint}/pets`,
      method: 'GET'
    });
    this.serverless.cli.log(util.inspect(r));
  }

  async getEndpoint () {
    /*
     Tweaks to code from:
      https://github.com/sbstjn/serverless-stack-output/blob/master/src/plugin.ts
    */
    const provider = this.serverless.getProvider('aws');
    const stackName = util.format('%s-%s',
      this.serverless.service.getServiceName(),
      this.serverless.getProvider('aws').getStage()
    );
    let response = await provider.request(
        'CloudFormation',
        'describeStacks',
        {StackName: stackName},
        provider.getStage(),
        provider.getRegion()
    );
    for (let output of response.Stacks[0].Outputs) {
      if (output['OutputKey'] === 'ServiceEndpoint') {
        return output['OutputValue'];
      }
    }
    throw "Could not locate service endpoint.";
  }

}

module.exports = ServerlessPlugin;
