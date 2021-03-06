# coding:utf-8
#
# This file is part of Forward.
#
# Forward is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Forward is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
-----Introduction-----
[Core][forward] Device class for c6509.
"""

from forward.devclass.baseCisco import BASECISCO


class C6509(BASECISCO):
    """This is a manufacturer of cisco, using the
    SSHV2 version of the protocol, so it is integrated with BASESSHV2 library.
    """

    def addUser(self, username, password):
        """Because the device of this model is different from the other Cisco
        devices in creating user parameters, it is rewritten.
        """
        return BASECISCO.addUser(self,
                                 username=username,
                                 password=password,
                                 addCommand='username {username} secret {password}\n')

    def changePassword(self, username, password):
        """Because the device of this model is different from the other
        Cisco devices in deleting user parameters, it is rewritten.
        """
        return BASECISCO.addUser(self,
                                 username=username,
                                 password=password,
                                 addCommand='username {username} secret {password}\n')
