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


class TrendingEntryDestinyRitual(object):
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
        'image': 'str',
        'icon': 'str',
        'title': 'str',
        'subtitle': 'str',
        'date_start': 'datetime',
        'date_end': 'datetime',
        'milestone_details': 'DestinyPublicMilestone',
        'event_content': 'DestinyMilestoneContent'
    }

    attribute_map = {
        'image': 'image',
        'icon': 'icon',
        'title': 'title',
        'subtitle': 'subtitle',
        'date_start': 'dateStart',
        'date_end': 'dateEnd',
        'milestone_details': 'milestoneDetails',
        'event_content': 'eventContent'
    }

    def __init__(self, image=None, icon=None, title=None, subtitle=None, date_start=None, date_end=None, milestone_details=None, event_content=None):  # noqa: E501
        """TrendingEntryDestinyRitual - a model defined in OpenAPI"""  # noqa: E501

        self._image = None
        self._icon = None
        self._title = None
        self._subtitle = None
        self._date_start = None
        self._date_end = None
        self._milestone_details = None
        self._event_content = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if icon is not None:
            self.icon = icon
        if title is not None:
            self.title = title
        if subtitle is not None:
            self.subtitle = subtitle
        self.date_start = date_start
        self.date_end = date_end
        if milestone_details is not None:
            self.milestone_details = milestone_details
        if event_content is not None:
            self.event_content = event_content

    @property
    def image(self):
        """Gets the image of this TrendingEntryDestinyRitual.  # noqa: E501


        :return: The image of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TrendingEntryDestinyRitual.


        :param image: The image of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def icon(self):
        """Gets the icon of this TrendingEntryDestinyRitual.  # noqa: E501


        :return: The icon of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this TrendingEntryDestinyRitual.


        :param icon: The icon of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def title(self):
        """Gets the title of this TrendingEntryDestinyRitual.  # noqa: E501


        :return: The title of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TrendingEntryDestinyRitual.


        :param title: The title of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def subtitle(self):
        """Gets the subtitle of this TrendingEntryDestinyRitual.  # noqa: E501


        :return: The subtitle of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this TrendingEntryDestinyRitual.


        :param subtitle: The subtitle of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

    @property
    def date_start(self):
        """Gets the date_start of this TrendingEntryDestinyRitual.  # noqa: E501


        :return: The date_start of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this TrendingEntryDestinyRitual.


        :param date_start: The date_start of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: datetime
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this TrendingEntryDestinyRitual.  # noqa: E501


        :return: The date_end of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: datetime
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this TrendingEntryDestinyRitual.


        :param date_end: The date_end of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: datetime
        """

        self._date_end = date_end

    @property
    def milestone_details(self):
        """Gets the milestone_details of this TrendingEntryDestinyRitual.  # noqa: E501

        A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.  # noqa: E501

        :return: The milestone_details of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: DestinyPublicMilestone
        """
        return self._milestone_details

    @milestone_details.setter
    def milestone_details(self, milestone_details):
        """Sets the milestone_details of this TrendingEntryDestinyRitual.

        A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.  # noqa: E501

        :param milestone_details: The milestone_details of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: DestinyPublicMilestone
        """

        self._milestone_details = milestone_details

    @property
    def event_content(self):
        """Gets the event_content of this TrendingEntryDestinyRitual.  # noqa: E501

        A destiny event will not necessarily have milestone \"custom content\", but if it does the details will be here.  # noqa: E501

        :return: The event_content of this TrendingEntryDestinyRitual.  # noqa: E501
        :rtype: DestinyMilestoneContent
        """
        return self._event_content

    @event_content.setter
    def event_content(self, event_content):
        """Sets the event_content of this TrendingEntryDestinyRitual.

        A destiny event will not necessarily have milestone \"custom content\", but if it does the details will be here.  # noqa: E501

        :param event_content: The event_content of this TrendingEntryDestinyRitual.  # noqa: E501
        :type: DestinyMilestoneContent
        """

        self._event_content = event_content

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
        if not isinstance(other, TrendingEntryDestinyRitual):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
