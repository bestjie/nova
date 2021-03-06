# Copyright (c) 2012 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import webob.exc

from nova.api.openstack import extensions
from nova.api.openstack import wsgi

ALIAS = "os-certificates"


class CertificatesController(wsgi.Controller):
    """The x509 Certificates API controller for the OpenStack API."""

    @extensions.expected_errors(410)
    def show(self, req, id):
        """Return certificate information."""
        raise webob.exc.HTTPGone()

    @extensions.expected_errors((410))
    def create(self, req, body=None):
        """Create a certificate."""
        raise webob.exc.HTTPGone()


class Certificates(extensions.V21APIExtensionBase):
    """Certificates support."""

    name = "Certificates"
    alias = ALIAS
    version = 1

    def get_resources(self):
        resources = [
            extensions.ResourceExtension(ALIAS,
                                         CertificatesController(),
                                         member_actions={})]
        return resources

    def get_controller_extensions(self):
        return []
