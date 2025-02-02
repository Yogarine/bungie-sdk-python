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


class ContentTypeProperty(object):
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
        'name': 'str',
        'readable_name': 'str',
        'value': 'str',
        'property_description': 'str',
        'localizable': 'bool',
        'fallback': 'bool',
        'enabled': 'bool',
        'order': 'int',
        'visible': 'bool',
        'is_title': 'bool',
        'required': 'bool',
        'max_length': 'int',
        'max_byte_length': 'int',
        'max_file_size': 'int',
        'regexp': 'str',
        'validate_as': 'str',
        'rss_attribute': 'str',
        'visible_dependency': 'str',
        'visible_on': 'str',
        'datatype': 'int',
        'attributes': 'dict(str, str)',
        'child_properties': 'list[ContentTypeProperty]',
        'content_type_allowed': 'str',
        'bind_to_property': 'str',
        'bound_regex': 'str',
        'representation_selection': 'dict(str, str)',
        'default_values': 'list[ContentTypeDefaultValue]',
        'is_external_allowed': 'bool',
        'property_section': 'str',
        'weight': 'int',
        'entitytype': 'str',
        'is_combo': 'bool',
        'suppress_property': 'bool',
        'legal_content_types': 'list[str]',
        'representation_validation_string': 'str',
        'min_width': 'int',
        'max_width': 'int',
        'min_height': 'int',
        'max_height': 'int',
        'is_video': 'bool',
        'is_image': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'readable_name': 'readableName',
        'value': 'value',
        'property_description': 'propertyDescription',
        'localizable': 'localizable',
        'fallback': 'fallback',
        'enabled': 'enabled',
        'order': 'order',
        'visible': 'visible',
        'is_title': 'isTitle',
        'required': 'required',
        'max_length': 'maxLength',
        'max_byte_length': 'maxByteLength',
        'max_file_size': 'maxFileSize',
        'regexp': 'regexp',
        'validate_as': 'validateAs',
        'rss_attribute': 'rssAttribute',
        'visible_dependency': 'visibleDependency',
        'visible_on': 'visibleOn',
        'datatype': 'datatype',
        'attributes': 'attributes',
        'child_properties': 'childProperties',
        'content_type_allowed': 'contentTypeAllowed',
        'bind_to_property': 'bindToProperty',
        'bound_regex': 'boundRegex',
        'representation_selection': 'representationSelection',
        'default_values': 'defaultValues',
        'is_external_allowed': 'isExternalAllowed',
        'property_section': 'propertySection',
        'weight': 'weight',
        'entitytype': 'entitytype',
        'is_combo': 'isCombo',
        'suppress_property': 'suppressProperty',
        'legal_content_types': 'legalContentTypes',
        'representation_validation_string': 'representationValidationString',
        'min_width': 'minWidth',
        'max_width': 'maxWidth',
        'min_height': 'minHeight',
        'max_height': 'maxHeight',
        'is_video': 'isVideo',
        'is_image': 'isImage'
    }

    def __init__(self, name=None, readable_name=None, value=None, property_description=None, localizable=None, fallback=None, enabled=None, order=None, visible=None, is_title=None, required=None, max_length=None, max_byte_length=None, max_file_size=None, regexp=None, validate_as=None, rss_attribute=None, visible_dependency=None, visible_on=None, datatype=None, attributes=None, child_properties=None, content_type_allowed=None, bind_to_property=None, bound_regex=None, representation_selection=None, default_values=None, is_external_allowed=None, property_section=None, weight=None, entitytype=None, is_combo=None, suppress_property=None, legal_content_types=None, representation_validation_string=None, min_width=None, max_width=None, min_height=None, max_height=None, is_video=None, is_image=None):  # noqa: E501
        """ContentTypeProperty - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._readable_name = None
        self._value = None
        self._property_description = None
        self._localizable = None
        self._fallback = None
        self._enabled = None
        self._order = None
        self._visible = None
        self._is_title = None
        self._required = None
        self._max_length = None
        self._max_byte_length = None
        self._max_file_size = None
        self._regexp = None
        self._validate_as = None
        self._rss_attribute = None
        self._visible_dependency = None
        self._visible_on = None
        self._datatype = None
        self._attributes = None
        self._child_properties = None
        self._content_type_allowed = None
        self._bind_to_property = None
        self._bound_regex = None
        self._representation_selection = None
        self._default_values = None
        self._is_external_allowed = None
        self._property_section = None
        self._weight = None
        self._entitytype = None
        self._is_combo = None
        self._suppress_property = None
        self._legal_content_types = None
        self._representation_validation_string = None
        self._min_width = None
        self._max_width = None
        self._min_height = None
        self._max_height = None
        self._is_video = None
        self._is_image = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if readable_name is not None:
            self.readable_name = readable_name
        if value is not None:
            self.value = value
        if property_description is not None:
            self.property_description = property_description
        if localizable is not None:
            self.localizable = localizable
        if fallback is not None:
            self.fallback = fallback
        if enabled is not None:
            self.enabled = enabled
        if order is not None:
            self.order = order
        if visible is not None:
            self.visible = visible
        if is_title is not None:
            self.is_title = is_title
        if required is not None:
            self.required = required
        if max_length is not None:
            self.max_length = max_length
        if max_byte_length is not None:
            self.max_byte_length = max_byte_length
        if max_file_size is not None:
            self.max_file_size = max_file_size
        if regexp is not None:
            self.regexp = regexp
        if validate_as is not None:
            self.validate_as = validate_as
        if rss_attribute is not None:
            self.rss_attribute = rss_attribute
        if visible_dependency is not None:
            self.visible_dependency = visible_dependency
        if visible_on is not None:
            self.visible_on = visible_on
        if datatype is not None:
            self.datatype = datatype
        if attributes is not None:
            self.attributes = attributes
        if child_properties is not None:
            self.child_properties = child_properties
        if content_type_allowed is not None:
            self.content_type_allowed = content_type_allowed
        if bind_to_property is not None:
            self.bind_to_property = bind_to_property
        if bound_regex is not None:
            self.bound_regex = bound_regex
        if representation_selection is not None:
            self.representation_selection = representation_selection
        if default_values is not None:
            self.default_values = default_values
        if is_external_allowed is not None:
            self.is_external_allowed = is_external_allowed
        if property_section is not None:
            self.property_section = property_section
        if weight is not None:
            self.weight = weight
        if entitytype is not None:
            self.entitytype = entitytype
        if is_combo is not None:
            self.is_combo = is_combo
        if suppress_property is not None:
            self.suppress_property = suppress_property
        if legal_content_types is not None:
            self.legal_content_types = legal_content_types
        if representation_validation_string is not None:
            self.representation_validation_string = representation_validation_string
        if min_width is not None:
            self.min_width = min_width
        if max_width is not None:
            self.max_width = max_width
        if min_height is not None:
            self.min_height = min_height
        if max_height is not None:
            self.max_height = max_height
        if is_video is not None:
            self.is_video = is_video
        if is_image is not None:
            self.is_image = is_image

    @property
    def name(self):
        """Gets the name of this ContentTypeProperty.  # noqa: E501


        :return: The name of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentTypeProperty.


        :param name: The name of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def readable_name(self):
        """Gets the readable_name of this ContentTypeProperty.  # noqa: E501


        :return: The readable_name of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._readable_name

    @readable_name.setter
    def readable_name(self, readable_name):
        """Sets the readable_name of this ContentTypeProperty.


        :param readable_name: The readable_name of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._readable_name = readable_name

    @property
    def value(self):
        """Gets the value of this ContentTypeProperty.  # noqa: E501


        :return: The value of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ContentTypeProperty.


        :param value: The value of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def property_description(self):
        """Gets the property_description of this ContentTypeProperty.  # noqa: E501


        :return: The property_description of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._property_description

    @property_description.setter
    def property_description(self, property_description):
        """Sets the property_description of this ContentTypeProperty.


        :param property_description: The property_description of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._property_description = property_description

    @property
    def localizable(self):
        """Gets the localizable of this ContentTypeProperty.  # noqa: E501


        :return: The localizable of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._localizable

    @localizable.setter
    def localizable(self, localizable):
        """Sets the localizable of this ContentTypeProperty.


        :param localizable: The localizable of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._localizable = localizable

    @property
    def fallback(self):
        """Gets the fallback of this ContentTypeProperty.  # noqa: E501


        :return: The fallback of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """Sets the fallback of this ContentTypeProperty.


        :param fallback: The fallback of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._fallback = fallback

    @property
    def enabled(self):
        """Gets the enabled of this ContentTypeProperty.  # noqa: E501


        :return: The enabled of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ContentTypeProperty.


        :param enabled: The enabled of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def order(self):
        """Gets the order of this ContentTypeProperty.  # noqa: E501


        :return: The order of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ContentTypeProperty.


        :param order: The order of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def visible(self):
        """Gets the visible of this ContentTypeProperty.  # noqa: E501


        :return: The visible of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ContentTypeProperty.


        :param visible: The visible of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def is_title(self):
        """Gets the is_title of this ContentTypeProperty.  # noqa: E501


        :return: The is_title of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._is_title

    @is_title.setter
    def is_title(self, is_title):
        """Sets the is_title of this ContentTypeProperty.


        :param is_title: The is_title of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._is_title = is_title

    @property
    def required(self):
        """Gets the required of this ContentTypeProperty.  # noqa: E501


        :return: The required of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ContentTypeProperty.


        :param required: The required of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def max_length(self):
        """Gets the max_length of this ContentTypeProperty.  # noqa: E501


        :return: The max_length of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ContentTypeProperty.


        :param max_length: The max_length of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def max_byte_length(self):
        """Gets the max_byte_length of this ContentTypeProperty.  # noqa: E501


        :return: The max_byte_length of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._max_byte_length

    @max_byte_length.setter
    def max_byte_length(self, max_byte_length):
        """Sets the max_byte_length of this ContentTypeProperty.


        :param max_byte_length: The max_byte_length of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._max_byte_length = max_byte_length

    @property
    def max_file_size(self):
        """Gets the max_file_size of this ContentTypeProperty.  # noqa: E501


        :return: The max_file_size of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, max_file_size):
        """Sets the max_file_size of this ContentTypeProperty.


        :param max_file_size: The max_file_size of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._max_file_size = max_file_size

    @property
    def regexp(self):
        """Gets the regexp of this ContentTypeProperty.  # noqa: E501


        :return: The regexp of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._regexp

    @regexp.setter
    def regexp(self, regexp):
        """Sets the regexp of this ContentTypeProperty.


        :param regexp: The regexp of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._regexp = regexp

    @property
    def validate_as(self):
        """Gets the validate_as of this ContentTypeProperty.  # noqa: E501


        :return: The validate_as of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._validate_as

    @validate_as.setter
    def validate_as(self, validate_as):
        """Sets the validate_as of this ContentTypeProperty.


        :param validate_as: The validate_as of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._validate_as = validate_as

    @property
    def rss_attribute(self):
        """Gets the rss_attribute of this ContentTypeProperty.  # noqa: E501


        :return: The rss_attribute of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._rss_attribute

    @rss_attribute.setter
    def rss_attribute(self, rss_attribute):
        """Sets the rss_attribute of this ContentTypeProperty.


        :param rss_attribute: The rss_attribute of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._rss_attribute = rss_attribute

    @property
    def visible_dependency(self):
        """Gets the visible_dependency of this ContentTypeProperty.  # noqa: E501


        :return: The visible_dependency of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._visible_dependency

    @visible_dependency.setter
    def visible_dependency(self, visible_dependency):
        """Sets the visible_dependency of this ContentTypeProperty.


        :param visible_dependency: The visible_dependency of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._visible_dependency = visible_dependency

    @property
    def visible_on(self):
        """Gets the visible_on of this ContentTypeProperty.  # noqa: E501


        :return: The visible_on of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._visible_on

    @visible_on.setter
    def visible_on(self, visible_on):
        """Sets the visible_on of this ContentTypeProperty.


        :param visible_on: The visible_on of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._visible_on = visible_on

    @property
    def datatype(self):
        """Gets the datatype of this ContentTypeProperty.  # noqa: E501


        :return: The datatype of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this ContentTypeProperty.


        :param datatype: The datatype of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._datatype = datatype

    @property
    def attributes(self):
        """Gets the attributes of this ContentTypeProperty.  # noqa: E501


        :return: The attributes of this ContentTypeProperty.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ContentTypeProperty.


        :param attributes: The attributes of this ContentTypeProperty.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def child_properties(self):
        """Gets the child_properties of this ContentTypeProperty.  # noqa: E501


        :return: The child_properties of this ContentTypeProperty.  # noqa: E501
        :rtype: list[ContentTypeProperty]
        """
        return self._child_properties

    @child_properties.setter
    def child_properties(self, child_properties):
        """Sets the child_properties of this ContentTypeProperty.


        :param child_properties: The child_properties of this ContentTypeProperty.  # noqa: E501
        :type: list[ContentTypeProperty]
        """

        self._child_properties = child_properties

    @property
    def content_type_allowed(self):
        """Gets the content_type_allowed of this ContentTypeProperty.  # noqa: E501


        :return: The content_type_allowed of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._content_type_allowed

    @content_type_allowed.setter
    def content_type_allowed(self, content_type_allowed):
        """Sets the content_type_allowed of this ContentTypeProperty.


        :param content_type_allowed: The content_type_allowed of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._content_type_allowed = content_type_allowed

    @property
    def bind_to_property(self):
        """Gets the bind_to_property of this ContentTypeProperty.  # noqa: E501


        :return: The bind_to_property of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._bind_to_property

    @bind_to_property.setter
    def bind_to_property(self, bind_to_property):
        """Sets the bind_to_property of this ContentTypeProperty.


        :param bind_to_property: The bind_to_property of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._bind_to_property = bind_to_property

    @property
    def bound_regex(self):
        """Gets the bound_regex of this ContentTypeProperty.  # noqa: E501


        :return: The bound_regex of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._bound_regex

    @bound_regex.setter
    def bound_regex(self, bound_regex):
        """Sets the bound_regex of this ContentTypeProperty.


        :param bound_regex: The bound_regex of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._bound_regex = bound_regex

    @property
    def representation_selection(self):
        """Gets the representation_selection of this ContentTypeProperty.  # noqa: E501


        :return: The representation_selection of this ContentTypeProperty.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._representation_selection

    @representation_selection.setter
    def representation_selection(self, representation_selection):
        """Sets the representation_selection of this ContentTypeProperty.


        :param representation_selection: The representation_selection of this ContentTypeProperty.  # noqa: E501
        :type: dict(str, str)
        """

        self._representation_selection = representation_selection

    @property
    def default_values(self):
        """Gets the default_values of this ContentTypeProperty.  # noqa: E501


        :return: The default_values of this ContentTypeProperty.  # noqa: E501
        :rtype: list[ContentTypeDefaultValue]
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this ContentTypeProperty.


        :param default_values: The default_values of this ContentTypeProperty.  # noqa: E501
        :type: list[ContentTypeDefaultValue]
        """

        self._default_values = default_values

    @property
    def is_external_allowed(self):
        """Gets the is_external_allowed of this ContentTypeProperty.  # noqa: E501


        :return: The is_external_allowed of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._is_external_allowed

    @is_external_allowed.setter
    def is_external_allowed(self, is_external_allowed):
        """Sets the is_external_allowed of this ContentTypeProperty.


        :param is_external_allowed: The is_external_allowed of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._is_external_allowed = is_external_allowed

    @property
    def property_section(self):
        """Gets the property_section of this ContentTypeProperty.  # noqa: E501


        :return: The property_section of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._property_section

    @property_section.setter
    def property_section(self, property_section):
        """Sets the property_section of this ContentTypeProperty.


        :param property_section: The property_section of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._property_section = property_section

    @property
    def weight(self):
        """Gets the weight of this ContentTypeProperty.  # noqa: E501


        :return: The weight of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ContentTypeProperty.


        :param weight: The weight of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def entitytype(self):
        """Gets the entitytype of this ContentTypeProperty.  # noqa: E501


        :return: The entitytype of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._entitytype

    @entitytype.setter
    def entitytype(self, entitytype):
        """Sets the entitytype of this ContentTypeProperty.


        :param entitytype: The entitytype of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._entitytype = entitytype

    @property
    def is_combo(self):
        """Gets the is_combo of this ContentTypeProperty.  # noqa: E501


        :return: The is_combo of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._is_combo

    @is_combo.setter
    def is_combo(self, is_combo):
        """Sets the is_combo of this ContentTypeProperty.


        :param is_combo: The is_combo of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._is_combo = is_combo

    @property
    def suppress_property(self):
        """Gets the suppress_property of this ContentTypeProperty.  # noqa: E501


        :return: The suppress_property of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_property

    @suppress_property.setter
    def suppress_property(self, suppress_property):
        """Sets the suppress_property of this ContentTypeProperty.


        :param suppress_property: The suppress_property of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._suppress_property = suppress_property

    @property
    def legal_content_types(self):
        """Gets the legal_content_types of this ContentTypeProperty.  # noqa: E501


        :return: The legal_content_types of this ContentTypeProperty.  # noqa: E501
        :rtype: list[str]
        """
        return self._legal_content_types

    @legal_content_types.setter
    def legal_content_types(self, legal_content_types):
        """Sets the legal_content_types of this ContentTypeProperty.


        :param legal_content_types: The legal_content_types of this ContentTypeProperty.  # noqa: E501
        :type: list[str]
        """

        self._legal_content_types = legal_content_types

    @property
    def representation_validation_string(self):
        """Gets the representation_validation_string of this ContentTypeProperty.  # noqa: E501


        :return: The representation_validation_string of this ContentTypeProperty.  # noqa: E501
        :rtype: str
        """
        return self._representation_validation_string

    @representation_validation_string.setter
    def representation_validation_string(self, representation_validation_string):
        """Sets the representation_validation_string of this ContentTypeProperty.


        :param representation_validation_string: The representation_validation_string of this ContentTypeProperty.  # noqa: E501
        :type: str
        """

        self._representation_validation_string = representation_validation_string

    @property
    def min_width(self):
        """Gets the min_width of this ContentTypeProperty.  # noqa: E501


        :return: The min_width of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._min_width

    @min_width.setter
    def min_width(self, min_width):
        """Sets the min_width of this ContentTypeProperty.


        :param min_width: The min_width of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._min_width = min_width

    @property
    def max_width(self):
        """Gets the max_width of this ContentTypeProperty.  # noqa: E501


        :return: The max_width of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """Sets the max_width of this ContentTypeProperty.


        :param max_width: The max_width of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._max_width = max_width

    @property
    def min_height(self):
        """Gets the min_height of this ContentTypeProperty.  # noqa: E501


        :return: The min_height of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._min_height

    @min_height.setter
    def min_height(self, min_height):
        """Sets the min_height of this ContentTypeProperty.


        :param min_height: The min_height of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._min_height = min_height

    @property
    def max_height(self):
        """Gets the max_height of this ContentTypeProperty.  # noqa: E501


        :return: The max_height of this ContentTypeProperty.  # noqa: E501
        :rtype: int
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """Sets the max_height of this ContentTypeProperty.


        :param max_height: The max_height of this ContentTypeProperty.  # noqa: E501
        :type: int
        """

        self._max_height = max_height

    @property
    def is_video(self):
        """Gets the is_video of this ContentTypeProperty.  # noqa: E501


        :return: The is_video of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._is_video

    @is_video.setter
    def is_video(self, is_video):
        """Sets the is_video of this ContentTypeProperty.


        :param is_video: The is_video of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._is_video = is_video

    @property
    def is_image(self):
        """Gets the is_image of this ContentTypeProperty.  # noqa: E501


        :return: The is_image of this ContentTypeProperty.  # noqa: E501
        :rtype: bool
        """
        return self._is_image

    @is_image.setter
    def is_image(self, is_image):
        """Sets the is_image of this ContentTypeProperty.


        :param is_image: The is_image of this ContentTypeProperty.  # noqa: E501
        :type: bool
        """

        self._is_image = is_image

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
        if not isinstance(other, ContentTypeProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
