# Copyright 2020 QuantInsti Quantitative Learnings Pvt Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import click
from piggin.s3.s3 import AwsS3
from piggin.utils.types import OSEnvAwsReset

CONTEXT_SETTINGS = dict(ignore_unknown_options=True,
                        allow_extra_args=True,
                        token_normalize_func=lambda x: x.lower())


@click.group()
@click.pass_context
def s3(ctx):
    """
        piggin s3 commands to interact with AWS s3 resources.
        
        Usage:\n
            piggin --help\n
            piggin s3 ls [options] path\n
            piggin s3 mkbucket [options] name\n
            piggin s3 mv [options] src dest\n
            piggin s3 cp [options] src dest\n
            piggin s3 rm [options] path\n
    """
    pass

@s3.command(context_settings=CONTEXT_SETTINGS)
@click.argument('path', default='s3:///')
@click.option(
    '--verbose/--silent',
    default=False,
    help='Turn on/ off verbosity. [verbose/silent]')
@click.pass_context
def ls(ctx, path, verbose):
    """
        list s3 buckets.
    """
    access_key = ctx.obj['access_key']
    secret_key = ctx.obj['secret_key']
    
    with OSEnvAwsReset(access_key, secret_key):
        awsS3 = AwsS3(access_key, secret_key)
        items = awsS3.ls(path)
        if items:
            print(items)
    
