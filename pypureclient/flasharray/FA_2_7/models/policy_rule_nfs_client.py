# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_7 import models

class PolicyRuleNfsClient(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access': 'str',
        'client': 'str',
        'name': 'str',
        'permission': 'str',
        'policy': 'FixedReferenceWithType'
    }

    attribute_map = {
        'access': 'access',
        'client': 'client',
        'name': 'name',
        'permission': 'permission',
        'policy': 'policy'
    }

    required_args = {
    }

    def __init__(
        self,
        access=None,  # type: str
        client=None,  # type: str
        name=None,  # type: str
        permission=None,  # type: str
        policy=None,  # type: models.FixedReferenceWithType
    ):
        """
        Keyword args:
            access (str): Specifies access control for the export. Valid values are `root-squash` and `no-root-squash`. The default is `root-squash` if not specified.
            client (str): Specifies the clients that will be permitted to access the export. Accepted notation includes IP, IP mask, or hostname. The default is `*` if not specified.
            name (str): Name of this rule. The name is automatically generated by the system.
            permission (str): Specifies which read-write client access permissions are allowed for the export. Valid values are `rw` and `ro`. The default is `rw` if not specified.
            policy (FixedReferenceWithType): The policy to which this rule belongs.
        """
        if access is not None:
            self.access = access
        if client is not None:
            self.client = client
        if name is not None:
            self.name = name
        if permission is not None:
            self.permission = permission
        if policy is not None:
            self.policy = policy

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicyRuleNfsClient`".format(key))
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
        if issubclass(PolicyRuleNfsClient, dict):
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
        if not isinstance(other, PolicyRuleNfsClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
