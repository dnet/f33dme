# This file is part of f33dme.
#
#  f33dme is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  le(n)x is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with f33dme.  If not, see <http://www.gnu.org/licenses/>.
#
# (C) 2010- by Adam Tauber, <asciimoo@gmail.com>

from django.contrib import admin
from f33dme.models import Feed, Item

class FeedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feed, FeedAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)

