# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tackerclient.tacker import v1_0 as tackerV10

_VNFBACKUP = 'vnfbackup'
_VNFRESTORE = 'vnfrestore'

class CreateBackup(tackerV10.CreateCommand):
    """Create a Backup."""

    resource = _VNFBACKUP

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', metavar='NAME',
            help='Set a name for the Backup')
        parser.add_argument(
            '--action',
            help='Set a actionfor the VNF')
        parser.add_argument(
            '--nova-instance-id',
            help='Set a nova instacne id for the VNF')
        # name + backup-name
        parser.add_argument(
            '--backup-name',
            help='Set a name for the VNF')
        parser.add_argument(
            '--container',
            help='Set a name for backup container in swift')
        parser.add_argument(
            '--storage',
            help='Set a name for repository')
        parser.add_argument(
            '--start-time',
            help='Set a start-time for backup')
        parser.add_argument(
            '--end-time',
            help='Set a end-time for backup')
        parser.add_argument(
            '--interval',
            help='Set a interval for backup')






    def args2body(self, parsed_args):
        body = {self.resource: {}}
        tacker_client = self.get_client()
        tacker_client.format = parsed_args.request_format


        tackerV10.update_dict(parsed_args, body[self.resource],
                              ['id', 'name', 'tenant_id','action','nova_instance_id','backup_name',
                               'container', 'storage','start_time','end_time','interval'])

        return body






#
# class ListCluster(tackerV10.ListCommand):
#     """List Clusters that belong to a given tenant."""
#
#     resource = _VNFCLUSTER
#     list_columns = ['id', 'name', 'status']
#
#
# class ShowCluster(tackerV10.ShowCommand):
#     """Show information of a given Cluster."""
#
#     resource = _VNFCLUSTER
#
#
# class DeleteCluster(tackerV10.DeleteCommand):
#     """Delete a given Cluster."""
#
#     resource = _VNFCLUSTER


