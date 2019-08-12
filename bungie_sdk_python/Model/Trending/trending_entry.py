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


class TrendingEntry(object):
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
        'weight': 'float',
        'is_featured': 'bool',
        'identifier': 'str',
        'entity_type': 'int',
        'display_name': 'str',
        'tagline': 'str',
        'image': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'link': 'str',
        'webm_video': 'str',
        'mp4_video': 'str',
        'feature_image': 'str',
        'items': 'list[TrendingEntry]',
        'creation_date': 'datetime'
    }

    attribute_map = {
        'weight': 'weight',
        'is_featured': 'isFeatured',
        'identifier': 'identifier',
        'entity_type': 'entityType',
        'display_name': 'displayName',
        'tagline': 'tagline',
        'image': 'image',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'link': 'link',
        'webm_video': 'webmVideo',
        'mp4_video': 'mp4Video',
        'feature_image': 'featureImage',
        'items': 'items',
        'creation_date': 'creationDate'
    }

    def __init__(self, weight=None, is_featured=None, identifier=None, entity_type=None, display_name=None, tagline=None, image=None, start_date=None, end_date=None, link=None, webm_video=None, mp4_video=None, feature_image=None, items=None, creation_date=None):  # noqa: E501
        """TrendingEntry - a model defined in OpenAPI"""  # noqa: E501

        self._weight = None
        self._is_featured = None
        self._identifier = None
        self._entity_type = None
        self._display_name = None
        self._tagline = None
        self._image = None
        self._start_date = None
        self._end_date = None
        self._link = None
        self._webm_video = None
        self._mp4_video = None
        self._feature_image = None
        self._items = None
        self._creation_date = None
        self.discriminator = None

        if weight is not None:
            self.weight = weight
        if is_featured is not None:
            self.is_featured = is_featured
        if identifier is not None:
            self.identifier = identifier
        if entity_type is not None:
            self.entity_type = entity_type
        if display_name is not None:
            self.display_name = display_name
        if tagline is not None:
            self.tagline = tagline
        if image is not None:
            self.image = image
        self.start_date = start_date
        self.end_date = end_date
        if link is not None:
            self.link = link
        if webm_video is not None:
            self.webm_video = webm_video
        if mp4_video is not None:
            self.mp4_video = mp4_video
        if feature_image is not None:
            self.feature_image = feature_image
        if items is not None:
            self.items = items
        self.creation_date = creation_date

    @property
    def weight(self):
        """Gets the weight of this TrendingEntry.  # noqa: E501

        The weighted score of this trending item.  # noqa: E501

        :return: The weight of this TrendingEntry.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this TrendingEntry.

        The weighted score of this trending item.  # noqa: E501

        :param weight: The weight of this TrendingEntry.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def is_featured(self):
        """Gets the is_featured of this TrendingEntry.  # noqa: E501


        :return: The is_featured of this TrendingEntry.  # noqa: E501
        :rtype: bool
        """
        return self._is_featured

    @is_featured.setter
    def is_featured(self, is_featured):
        """Sets the is_featured of this TrendingEntry.


        :param is_featured: The is_featured of this TrendingEntry.  # noqa: E501
        :type: bool
        """

        self._is_featured = is_featured

    @property
    def identifier(self):
        """Gets the identifier of this TrendingEntry.  # noqa: E501

        We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.  # noqa: E501

        :return: The identifier of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this TrendingEntry.

        We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.  # noqa: E501

        :param identifier: The identifier of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def entity_type(self):
        """Gets the entity_type of this TrendingEntry.  # noqa: E501

        An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.  # noqa: E501

        :return: The entity_type of this TrendingEntry.  # noqa: E501
        :rtype: int
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this TrendingEntry.

        An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.  # noqa: E501

        :param entity_type: The entity_type of this TrendingEntry.  # noqa: E501
        :type: int
        """

        self._entity_type = entity_type

    @property
    def display_name(self):
        """Gets the display_name of this TrendingEntry.  # noqa: E501

        The localized \"display name/article title/'primary localized identifier'\" of the entity.  # noqa: E501

        :return: The display_name of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TrendingEntry.

        The localized \"display name/article title/'primary localized identifier'\" of the entity.  # noqa: E501

        :param display_name: The display_name of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def tagline(self):
        """Gets the tagline of this TrendingEntry.  # noqa: E501

        If the entity has a localized tagline/subtitle/motto/whatever, that is found here.  # noqa: E501

        :return: The tagline of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._tagline

    @tagline.setter
    def tagline(self, tagline):
        """Sets the tagline of this TrendingEntry.

        If the entity has a localized tagline/subtitle/motto/whatever, that is found here.  # noqa: E501

        :param tagline: The tagline of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._tagline = tagline

    @property
    def image(self):
        """Gets the image of this TrendingEntry.  # noqa: E501


        :return: The image of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TrendingEntry.


        :param image: The image of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def start_date(self):
        """Gets the start_date of this TrendingEntry.  # noqa: E501


        :return: The start_date of this TrendingEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TrendingEntry.


        :param start_date: The start_date of this TrendingEntry.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TrendingEntry.  # noqa: E501


        :return: The end_date of this TrendingEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TrendingEntry.


        :param end_date: The end_date of this TrendingEntry.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def link(self):
        """Gets the link of this TrendingEntry.  # noqa: E501


        :return: The link of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TrendingEntry.


        :param link: The link of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def webm_video(self):
        """Gets the webm_video of this TrendingEntry.  # noqa: E501

        If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo  # noqa: E501

        :return: The webm_video of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._webm_video

    @webm_video.setter
    def webm_video(self, webm_video):
        """Sets the webm_video of this TrendingEntry.

        If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo  # noqa: E501

        :param webm_video: The webm_video of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._webm_video = webm_video

    @property
    def mp4_video(self):
        """Gets the mp4_video of this TrendingEntry.  # noqa: E501

        If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo  # noqa: E501

        :return: The mp4_video of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._mp4_video

    @mp4_video.setter
    def mp4_video(self, mp4_video):
        """Sets the mp4_video of this TrendingEntry.

        If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo  # noqa: E501

        :param mp4_video: The mp4_video of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._mp4_video = mp4_video

    @property
    def feature_image(self):
        """Gets the feature_image of this TrendingEntry.  # noqa: E501

        If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.  # noqa: E501

        :return: The feature_image of this TrendingEntry.  # noqa: E501
        :rtype: str
        """
        return self._feature_image

    @feature_image.setter
    def feature_image(self, feature_image):
        """Sets the feature_image of this TrendingEntry.

        If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.  # noqa: E501

        :param feature_image: The feature_image of this TrendingEntry.  # noqa: E501
        :type: str
        """

        self._feature_image = feature_image

    @property
    def items(self):
        """Gets the items of this TrendingEntry.  # noqa: E501

        If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header.  # noqa: E501

        :return: The items of this TrendingEntry.  # noqa: E501
        :rtype: list[TrendingEntry]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this TrendingEntry.

        If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header.  # noqa: E501

        :param items: The items of this TrendingEntry.  # noqa: E501
        :type: list[TrendingEntry]
        """

        self._items = items

    @property
    def creation_date(self):
        """Gets the creation_date of this TrendingEntry.  # noqa: E501

        If the entry has a date at which it was created, this is that date.  # noqa: E501

        :return: The creation_date of this TrendingEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this TrendingEntry.

        If the entry has a date at which it was created, this is that date.  # noqa: E501

        :param creation_date: The creation_date of this TrendingEntry.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

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
        if not isinstance(other, TrendingEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other