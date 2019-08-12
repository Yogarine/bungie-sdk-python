# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.  # noqa: E501

    OpenAPI spec version: 2.3.6
    Contact: support@bungie.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DestinyVendorResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'vendor': 'SingleComponentResponseOfDestinyVendorComponent',
        'categories': 'SingleComponentResponseOfDestinyVendorCategoriesComponent',
        'sales': 'DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent',
        'item_components': 'DestinyItemComponentSetOfint32',
        'currency_lookups': 'SingleComponentResponseOfDestinyCurrenciesComponent'
    }

    attribute_map = {
        'vendor': 'vendor',
        'categories': 'categories',
        'sales': 'sales',
        'item_components': 'itemComponents',
        'currency_lookups': 'currencyLookups'
    }

    def __init__(self, vendor=None, categories=None, sales=None, item_components=None, currency_lookups=None):  # noqa: E501
        """DestinyVendorResponse - a model defined in OpenAPI"""  # noqa: E501

        self._vendor = None
        self._categories = None
        self._sales = None
        self._item_components = None
        self._currency_lookups = None
        self.discriminator = None

        if vendor is not None:
            self.vendor = vendor
        if categories is not None:
            self.categories = categories
        if sales is not None:
            self.sales = sales
        if item_components is not None:
            self.item_components = item_components
        if currency_lookups is not None:
            self.currency_lookups = currency_lookups

    @property
    def vendor(self):
        """Gets the vendor of this DestinyVendorResponse.  # noqa: E501

        The base properties of the vendor.  COMPONENT TYPE: Vendors  # noqa: E501

        :return: The vendor of this DestinyVendorResponse.  # noqa: E501
        :rtype: SingleComponentResponseOfDestinyVendorComponent
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this DestinyVendorResponse.

        The base properties of the vendor.  COMPONENT TYPE: Vendors  # noqa: E501

        :param vendor: The vendor of this DestinyVendorResponse.  # noqa: E501
        :type: SingleComponentResponseOfDestinyVendorComponent
        """

        self._vendor = vendor

    @property
    def categories(self):
        """Gets the categories of this DestinyVendorResponse.  # noqa: E501

        Categories that the vendor has available, and references to the sales therein.  COMPONENT TYPE: VendorCategories  # noqa: E501

        :return: The categories of this DestinyVendorResponse.  # noqa: E501
        :rtype: SingleComponentResponseOfDestinyVendorCategoriesComponent
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this DestinyVendorResponse.

        Categories that the vendor has available, and references to the sales therein.  COMPONENT TYPE: VendorCategories  # noqa: E501

        :param categories: The categories of this DestinyVendorResponse.  # noqa: E501
        :type: SingleComponentResponseOfDestinyVendorCategoriesComponent
        """

        self._categories = categories

    @property
    def sales(self):
        """Gets the sales of this DestinyVendorResponse.  # noqa: E501

        Sales, keyed by the vendorItemIndex of the item being sold.  COMPONENT TYPE: VendorSales  # noqa: E501

        :return: The sales of this DestinyVendorResponse.  # noqa: E501
        :rtype: DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent
        """
        return self._sales

    @sales.setter
    def sales(self, sales):
        """Sets the sales of this DestinyVendorResponse.

        Sales, keyed by the vendorItemIndex of the item being sold.  COMPONENT TYPE: VendorSales  # noqa: E501

        :param sales: The sales of this DestinyVendorResponse.  # noqa: E501
        :type: DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent
        """

        self._sales = sales

    @property
    def item_components(self):
        """Gets the item_components of this DestinyVendorResponse.  # noqa: E501

        Item components, keyed by the vendorItemIndex of the active sale items.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]  # noqa: E501

        :return: The item_components of this DestinyVendorResponse.  # noqa: E501
        :rtype: DestinyItemComponentSetOfint32
        """
        return self._item_components

    @item_components.setter
    def item_components(self, item_components):
        """Sets the item_components of this DestinyVendorResponse.

        Item components, keyed by the vendorItemIndex of the active sale items.  COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]  # noqa: E501

        :param item_components: The item_components of this DestinyVendorResponse.  # noqa: E501
        :type: DestinyItemComponentSetOfint32
        """

        self._item_components = item_components

    @property
    def currency_lookups(self):
        """Gets the currency_lookups of this DestinyVendorResponse.  # noqa: E501

        A \"lookup\" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.  COMPONENT TYPE: CurrencyLookups  # noqa: E501

        :return: The currency_lookups of this DestinyVendorResponse.  # noqa: E501
        :rtype: SingleComponentResponseOfDestinyCurrenciesComponent
        """
        return self._currency_lookups

    @currency_lookups.setter
    def currency_lookups(self, currency_lookups):
        """Sets the currency_lookups of this DestinyVendorResponse.

        A \"lookup\" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.  COMPONENT TYPE: CurrencyLookups  # noqa: E501

        :param currency_lookups: The currency_lookups of this DestinyVendorResponse.  # noqa: E501
        :type: SingleComponentResponseOfDestinyCurrenciesComponent
        """

        self._currency_lookups = currency_lookups

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, DestinyVendorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other