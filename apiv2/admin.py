# -*- coding: utf-8 -*-

#
# Freesound is (c) MUSIC TECHNOLOGY GROUP, UNIVERSITAT POMPEU FABRA
#
# Freesound is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Freesound is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     See AUTHORS file.
#

from django.contrib import admin
from apiv2.models import ApiV2Client


class ApiV2ClientAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    search_fields = ('=user__username', )
    list_filter = ('status', )
    list_display = ("user", "client_id", "client_secret", "oauth_client", "status", "allow_oauth_passoword_grant")

admin.site.register(ApiV2Client, ApiV2ClientAdmin)