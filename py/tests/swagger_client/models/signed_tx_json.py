# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.  # noqa: E501

    OpenAPI spec version: 0.8.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.encoded_hash import EncodedHash  # noqa: F401,E501
from swagger_client.models.json_tx import JSONTx  # noqa: F401,E501


class SignedTxJSON(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tx': 'JSONTx',
        'block_height': 'int',
        'block_hash': 'EncodedHash',
        'hash': 'EncodedHash',
        'signatures': 'list[str]'
    }

    attribute_map = {
        'tx': 'tx',
        'block_height': 'block_height',
        'block_hash': 'block_hash',
        'hash': 'hash',
        'signatures': 'signatures'
    }

    def __init__(self, tx=None, block_height=None, block_hash=None, hash=None, signatures=None):  # noqa: E501
        """SignedTxJSON - a model defined in Swagger"""  # noqa: E501

        self._tx = None
        self._block_height = None
        self._block_hash = None
        self._hash = None
        self._signatures = None
        self.discriminator = None

        if tx is not None:
            self.tx = tx
        if block_height is not None:
            self.block_height = block_height
        if block_hash is not None:
            self.block_hash = block_hash
        if hash is not None:
            self.hash = hash
        if signatures is not None:
            self.signatures = signatures

    @property
    def tx(self):
        """Gets the tx of this SignedTxJSON.  # noqa: E501


        :return: The tx of this SignedTxJSON.  # noqa: E501
        :rtype: JSONTx
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """Sets the tx of this SignedTxJSON.


        :param tx: The tx of this SignedTxJSON.  # noqa: E501
        :type: JSONTx
        """

        self._tx = tx

    @property
    def block_height(self):
        """Gets the block_height of this SignedTxJSON.  # noqa: E501


        :return: The block_height of this SignedTxJSON.  # noqa: E501
        :rtype: int
        """
        return self._block_height

    @block_height.setter
    def block_height(self, block_height):
        """Sets the block_height of this SignedTxJSON.


        :param block_height: The block_height of this SignedTxJSON.  # noqa: E501
        :type: int
        """

        self._block_height = block_height

    @property
    def block_hash(self):
        """Gets the block_hash of this SignedTxJSON.  # noqa: E501


        :return: The block_hash of this SignedTxJSON.  # noqa: E501
        :rtype: EncodedHash
        """
        return self._block_hash

    @block_hash.setter
    def block_hash(self, block_hash):
        """Sets the block_hash of this SignedTxJSON.


        :param block_hash: The block_hash of this SignedTxJSON.  # noqa: E501
        :type: EncodedHash
        """

        self._block_hash = block_hash

    @property
    def hash(self):
        """Gets the hash of this SignedTxJSON.  # noqa: E501


        :return: The hash of this SignedTxJSON.  # noqa: E501
        :rtype: EncodedHash
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this SignedTxJSON.


        :param hash: The hash of this SignedTxJSON.  # noqa: E501
        :type: EncodedHash
        """

        self._hash = hash

    @property
    def signatures(self):
        """Gets the signatures of this SignedTxJSON.  # noqa: E501


        :return: The signatures of this SignedTxJSON.  # noqa: E501
        :rtype: list[str]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this SignedTxJSON.


        :param signatures: The signatures of this SignedTxJSON.  # noqa: E501
        :type: list[str]
        """

        self._signatures = signatures

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignedTxJSON):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
