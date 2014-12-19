# -*- coding: utf-8 -*-

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


from ryu import cfg
from ryu.base import app_manager
from ryu.lib import hub
from ryu.lib.xflow import sflow


opts = [cfg.StrOpt('address', default='0.0.0.0',
                   help='sFlow Collector bind address'),
        cfg.IntOpt('port', default=6343,
                   help='sFlow Collector port'),
        cfg.IntOpt('max_udp_msg_size', default=1472,
                   help='Maximum size of UDP messages')]

cfg.CONF.register_opts(opts, 'plow')


class SFlow(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(SFlow, self).__init__(*args, **kwargs)
        self._address = self.CONF.plow.address
        self._port = self.CONF.plow.port
        self._udp_msg_size = self.CONF.plow.max_udp_msg_size
        self._udp_sock = None

    def _handle(self, buf, addr):
        packet = sflow.sFlow.parser(buf)

        if not packet:
            return

        print packet.__dict__

    def _recv_loop(self):
        self.logger.info('Listening on %s:%s for sflow agents' %
                         (self._address, self._port))

        while True:
            buf, addr = self._udp_sock.recvfrom(self._udp_msg_size)
            t = hub.spawn(self._handle, buf, addr)
            self.threads.append(t)

    def start(self):
        self._udp_sock = hub.socket.socket(hub.socket.AF_INET,
                                           hub.socket.SOCK_DGRAM)
        self._udp_sock.bind((self._address, self._port))

        t = hub.spawn(self._recv_loop)
        super(SFlow, self).start()
        return t
