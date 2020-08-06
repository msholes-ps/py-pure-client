# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_1 import models

class FileSystem(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'id': 'str',
        'name': 'str',
        'arrays': 'list[FixedReferenceFqdn]',
        'created': 'int',
        'destroyed': 'bool',
        'fast_remove_directory_enabled': 'bool',
        'hard_limit_enabled': 'bool',
        'http': 'Http',
        'nfs': 'Nfs',
        'provisioned': 'int',
        'smb': 'Smb',
        'snapshot_directory_enabled': 'bool'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'name': 'name',
        'arrays': 'arrays',
        'created': 'created',
        'destroyed': 'destroyed',
        'fast_remove_directory_enabled': 'fast_remove_directory_enabled',
        'hard_limit_enabled': 'hard_limit_enabled',
        'http': 'http',
        'nfs': 'nfs',
        'provisioned': 'provisioned',
        'smb': 'smb',
        'snapshot_directory_enabled': 'snapshot_directory_enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        name=None,  # type: str
        arrays=None,  # type: List[models.FixedReferenceFqdn]
        created=None,  # type: int
        destroyed=None,  # type: bool
        fast_remove_directory_enabled=None,  # type: bool
        hard_limit_enabled=None,  # type: bool
        http=None,  # type: models.Http
        nfs=None,  # type: models.Nfs
        provisioned=None,  # type: int
        smb=None,  # type: models.Smb
        snapshot_directory_enabled=None,  # type: bool
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            name (str): A non-modifiable, locally unique name chosen by the system.
            arrays (list[FixedReferenceFqdn]): The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.
            created (int): Creation time in milliseconds since UNIX epoch.
            destroyed (bool): Is the file system destroyed?
            fast_remove_directory_enabled (bool): Is fast remove directory enabled?
            hard_limit_enabled (bool): Is the file system's size a hard limit quota?
            http (Http): HTTP configuration.
            nfs (Nfs): NFS configuration.
            provisioned (int): The provisioned size of the file system in bytes. A value of 0 means unlimited.
            smb (Smb): SMB configuration.
            snapshot_directory_enabled (bool): Is snapshot directory enabled?
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if arrays is not None:
            self.arrays = arrays
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if fast_remove_directory_enabled is not None:
            self.fast_remove_directory_enabled = fast_remove_directory_enabled
        if hard_limit_enabled is not None:
            self.hard_limit_enabled = hard_limit_enabled
        if http is not None:
            self.http = http
        if nfs is not None:
            self.nfs = nfs
        if provisioned is not None:
            self.provisioned = provisioned
        if smb is not None:
            self.smb = smb
        if snapshot_directory_enabled is not None:
            self.snapshot_directory_enabled = snapshot_directory_enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `FileSystem`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(FileSystem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
