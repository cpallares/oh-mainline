#!/usr/bin/env python
#
# Copyright (C) 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# This module is used for version 2 of the Google Data APIs.


__author__ = 'j.s@google.com (Jeff Scudder)'


import unittest
import gdata.test_config as conf
import gdata.data
import gdata.acl.data
import gdata.analytics.data
import gdata.dublincore.data
import gdata.books.data
import gdata.calendar.data
import gdata.geo.data
import gdata.finance.data
import gdata.notebook.data
import gdata.media.data
import gdata.youtube.data
import gdata.webmastertools.data
import gdata.contacts.data
import gdata.opensearch.data


class DataSmokeTest(unittest.TestCase):

  def test_check_all_data_classes(self):
    conf.check_data_classes(self, (
        gdata.data.TotalResults, gdata.data.StartIndex,
        gdata.data.ItemsPerPage, gdata.data.ExtendedProperty,
        gdata.data.GDEntry, gdata.data.GDFeed, gdata.data.BatchId,
        gdata.data.BatchOperation, gdata.data.BatchStatus,
        gdata.data.BatchEntry, gdata.data.BatchInterrupted,
        gdata.data.BatchFeed, gdata.data.EntryLink, gdata.data.FeedLink,
        gdata.data.AdditionalName, gdata.data.Comments, gdata.data.Country,
        gdata.data.Email, gdata.data.FamilyName, gdata.data.Im,
        gdata.data.GivenName, gdata.data.NamePrefix, gdata.data.NameSuffix,
        gdata.data.FullName, gdata.data.Name, gdata.data.OrgDepartment,
        gdata.data.OrgName, gdata.data.OrgSymbol, gdata.data.OrgTitle,
        gdata.data.Organization, gdata.data.When, gdata.data.Who,
        gdata.data.OriginalEvent, gdata.data.PhoneNumber,
        gdata.data.PostalAddress, gdata.data.Rating, gdata.data.Recurrence,
        gdata.data.RecurrenceException, gdata.data.Reminder,
        gdata.data.Agent, gdata.data.HouseName, gdata.data.Street,
        gdata.data.PoBox, gdata.data.Neighborhood, gdata.data.City,
        gdata.data.Subregion, gdata.data.Region, gdata.data.Postcode,
        gdata.data.Country, gdata.data.FormattedAddress,
        gdata.data.StructuredPostalAddress, gdata.data.Where,
        gdata.data.AttendeeType, gdata.data.AttendeeStatus,
        gdata.data.Deleted, gdata.data.Money,
        gdata.acl.data.AclRole, gdata.acl.data.AclScope,
        gdata.acl.data.AclWithKey,
        gdata.acl.data.AclEntry, gdata.acl.data.AclFeed,
        gdata.analytics.data.Dimension,
        gdata.analytics.data.EndDate,
        gdata.analytics.data.Metric,
        gdata.analytics.data.Aggregates,
        gdata.analytics.data.DataEntry,
        gdata.analytics.data.Property,
        gdata.analytics.data.StartDate,
        gdata.analytics.data.TableId,
        gdata.analytics.data.AccountEntry,
        gdata.analytics.data.TableName,
        gdata.analytics.data.DataSource,
        gdata.analytics.data.AccountFeed,
        gdata.analytics.data.DataFeed,
        gdata.dublincore.data.Creator,
        gdata.dublincore.data.Date,
        gdata.dublincore.data.Description,
        gdata.dublincore.data.Format,
        gdata.dublincore.data.Identifier,
        gdata.dublincore.data.Language,
        gdata.dublincore.data.Publisher,
        gdata.dublincore.data.Rights,
        gdata.dublincore.data.Subject,
        gdata.dublincore.data.Title,
        gdata.books.data.CollectionEntry,
        gdata.books.data.CollectionFeed,
        gdata.books.data.Embeddability,
        gdata.books.data.OpenAccess,
        gdata.books.data.Review,
        gdata.books.data.Viewability,
        gdata.books.data.VolumeEntry,
        gdata.books.data.VolumeFeed,
        gdata.calendar.data.AccessLevelProperty,
        gdata.calendar.data.AllowGSync2Property,
        gdata.calendar.data.AllowGSyncProperty,
        gdata.calendar.data.AnyoneCanAddSelfProperty,
        gdata.calendar.data.CalendarAclRole,
        gdata.calendar.data.CalendarCommentEntry,
        gdata.calendar.data.CalendarCommentFeed,
        gdata.calendar.data.CalendarComments,
        gdata.calendar.data.CalendarExtendedProperty,
        gdata.calendar.data.CalendarWhere,
        gdata.calendar.data.ColorProperty,
        gdata.calendar.data.GuestsCanInviteOthersProperty,
        gdata.calendar.data.GuestsCanModifyProperty,
        gdata.calendar.data.GuestsCanSeeGuestsProperty,
        gdata.calendar.data.HiddenProperty,
        gdata.calendar.data.IcalUIDProperty,
        gdata.calendar.data.OverrideNameProperty,
        gdata.calendar.data.PrivateCopyProperty,
        gdata.calendar.data.QuickAddProperty,
        gdata.calendar.data.ResourceProperty,
        gdata.calendar.data.EventWho,
        gdata.calendar.data.SelectedProperty,
        gdata.calendar.data.SendAclNotificationsProperty,
        gdata.calendar.data.CalendarAclEntry,
        gdata.calendar.data.CalendarAclFeed,
        gdata.calendar.data.SendEventNotificationsProperty,
        gdata.calendar.data.SequenceNumberProperty,
        gdata.calendar.data.CalendarRecurrenceExceptionEntry,
        gdata.calendar.data.CalendarRecurrenceException,
        gdata.calendar.data.SettingsProperty,
        gdata.calendar.data.SettingsEntry,
        gdata.calendar.data.CalendarSettingsFeed,
        gdata.calendar.data.SuppressReplyNotificationsProperty,
        gdata.calendar.data.SyncEventProperty,
        gdata.calendar.data.CalendarEventEntry,
        gdata.calendar.data.TimeZoneProperty,
        gdata.calendar.data.TimesCleanedProperty,
        gdata.calendar.data.CalendarEntry,
        gdata.calendar.data.CalendarEventFeed,
        gdata.calendar.data.CalendarFeed,
        gdata.calendar.data.WebContentGadgetPref,
        gdata.calendar.data.WebContent,
        gdata.finance.data.Commission,
        gdata.finance.data.CostBasis,
        gdata.finance.data.DaysGain,
        gdata.finance.data.Gain,
        gdata.finance.data.MarketValue,
        gdata.finance.data.PortfolioData,
        gdata.finance.data.PortfolioEntry,
        gdata.finance.data.PortfolioFeed,
        gdata.finance.data.PositionData,
        gdata.finance.data.Price,
        gdata.finance.data.Symbol,
        gdata.finance.data.PositionEntry,
        gdata.finance.data.PositionFeed,
        gdata.finance.data.TransactionData,
        gdata.finance.data.TransactionEntry,
        gdata.finance.data.TransactionFeed,
        gdata.notebook.data.ComesAfter,
        gdata.notebook.data.NoteEntry,
        gdata.notebook.data.NotebookFeed,
        gdata.notebook.data.NotebookListEntry,
        gdata.notebook.data.NotebookListFeed,
        gdata.youtube.data.ComplaintEntry,
        gdata.youtube.data.ComplaintFeed,
        gdata.youtube.data.RatingEntry,
        gdata.youtube.data.RatingFeed,
        gdata.youtube.data.YouTubeMediaContent,
        gdata.youtube.data.YtAge,
        gdata.youtube.data.YtBooks,
        gdata.youtube.data.YtCompany,
        gdata.youtube.data.YtDescription,
        gdata.youtube.data.YtDuration,
        gdata.youtube.data.YtFirstName,
        gdata.youtube.data.YtGender,
        gdata.youtube.data.YtHobbies,
        gdata.youtube.data.YtHometown,
        gdata.youtube.data.YtLastName,
        gdata.youtube.data.YtLocation,
        gdata.youtube.data.YtMovies,
        gdata.youtube.data.YtMusic,
        gdata.youtube.data.YtNoEmbed,
        gdata.youtube.data.YtOccupation,
        gdata.youtube.data.YtPlaylistId,
        gdata.youtube.data.YtPosition,
        gdata.youtube.data.YtPrivate,
        gdata.youtube.data.YtQueryString,
        gdata.youtube.data.YtRacy,
        gdata.youtube.data.YtRecorded,
        gdata.youtube.data.YtRelationship,
        gdata.youtube.data.YtSchool,
        gdata.youtube.data.YtStatistics,
        gdata.youtube.data.YtStatus,
        gdata.youtube.data.YtUserProfileStatistics,
        gdata.youtube.data.YtUsername,
        gdata.youtube.data.FriendEntry,
        gdata.youtube.data.FriendFeed,
        gdata.youtube.data.YtVideoStatistics,
        gdata.youtube.data.ChannelEntry,
        gdata.youtube.data.ChannelFeed,
        gdata.youtube.data.FavoriteEntry,
        gdata.youtube.data.FavoriteFeed,
        gdata.youtube.data.YouTubeMediaCredit,
        gdata.youtube.data.YouTubeMediaRating,
        gdata.youtube.data.YtAboutMe,
        gdata.youtube.data.UserProfileEntry,
        gdata.youtube.data.UserProfileFeed,
        gdata.youtube.data.YtAspectRatio,
        gdata.youtube.data.YtBasePublicationState,
        gdata.youtube.data.YtPublicationState,
        gdata.youtube.data.YouTubeAppControl,
        gdata.youtube.data.YtCaptionPublicationState,
        gdata.youtube.data.YouTubeCaptionAppControl,
        gdata.youtube.data.CaptionTrackEntry,
        gdata.youtube.data.CaptionTrackFeed,
        gdata.youtube.data.YtCountHint,
        gdata.youtube.data.PlaylistLinkEntry,
        gdata.youtube.data.PlaylistLinkFeed,
        gdata.youtube.data.YtModerationStatus,
        gdata.youtube.data.YtPlaylistTitle,
        gdata.youtube.data.SubscriptionEntry,
        gdata.youtube.data.SubscriptionFeed,
        gdata.youtube.data.YtSpam,
        gdata.youtube.data.CommentEntry,
        gdata.youtube.data.CommentFeed,
        gdata.youtube.data.YtUploaded,
        gdata.youtube.data.YtVideoId,
        gdata.youtube.data.YouTubeMediaGroup,
        gdata.youtube.data.VideoEntryBase,
        gdata.youtube.data.PlaylistEntry,
        gdata.youtube.data.PlaylistFeed,
        gdata.youtube.data.VideoEntry,
        gdata.youtube.data.VideoFeed,
        gdata.youtube.data.VideoMessageEntry,
        gdata.youtube.data.VideoMessageFeed,
        gdata.youtube.data.UserEventEntry,
        gdata.youtube.data.UserEventFeed,
        gdata.youtube.data.VideoModerationEntry,
        gdata.youtube.data.VideoModerationFeed,
        gdata.media.data.MediaCategory,
        gdata.media.data.MediaCopyright,
        gdata.media.data.MediaCredit,
        gdata.media.data.MediaDescription,
        gdata.media.data.MediaHash,
        gdata.media.data.MediaKeywords,
        gdata.media.data.MediaPlayer,
        gdata.media.data.MediaRating,
        gdata.media.data.MediaRestriction,
        gdata.media.data.MediaText,
        gdata.media.data.MediaThumbnail,
        gdata.media.data.MediaTitle,
        gdata.media.data.MediaContent,
        gdata.media.data.MediaGroup,
        gdata.webmastertools.data.CrawlIssueCrawlType,
        gdata.webmastertools.data.CrawlIssueDateDetected,
        gdata.webmastertools.data.CrawlIssueDetail,
        gdata.webmastertools.data.CrawlIssueIssueType,
        gdata.webmastertools.data.CrawlIssueLinkedFromUrl,
        gdata.webmastertools.data.CrawlIssueUrl,
        gdata.webmastertools.data.CrawlIssueEntry,
        gdata.webmastertools.data.CrawlIssuesFeed,
        gdata.webmastertools.data.Indexed,
        gdata.webmastertools.data.Keyword,
        gdata.webmastertools.data.KeywordEntry,
        gdata.webmastertools.data.KeywordsFeed,
        gdata.webmastertools.data.LastCrawled,
        gdata.webmastertools.data.MessageBody,
        gdata.webmastertools.data.MessageDate,
        gdata.webmastertools.data.MessageLanguage,
        gdata.webmastertools.data.MessageRead,
        gdata.webmastertools.data.MessageSubject,
        gdata.webmastertools.data.SiteId,
        gdata.webmastertools.data.MessageEntry,
        gdata.webmastertools.data.MessagesFeed,
        gdata.webmastertools.data.SitemapEntry,
        gdata.webmastertools.data.SitemapMobileMarkupLanguage,
        gdata.webmastertools.data.SitemapMobile,
        gdata.webmastertools.data.SitemapNewsPublicationLabel,
        gdata.webmastertools.data.SitemapNews,
        gdata.webmastertools.data.SitemapType,
        gdata.webmastertools.data.SitemapUrlCount,
        gdata.webmastertools.data.SitemapsFeed,
        gdata.webmastertools.data.VerificationMethod,
        gdata.webmastertools.data.Verified,
        gdata.webmastertools.data.SiteEntry,
        gdata.webmastertools.data.SitesFeed,
        gdata.contacts.data.BillingInformation,
        gdata.contacts.data.Birthday,
        gdata.contacts.data.CalendarLink,
        gdata.contacts.data.DirectoryServer,
        gdata.contacts.data.Event,
        gdata.contacts.data.ExternalId,
        gdata.contacts.data.Gender,
        gdata.contacts.data.Hobby,
        gdata.contacts.data.Initials,
        gdata.contacts.data.Jot,
        gdata.contacts.data.Language,
        gdata.contacts.data.MaidenName,
        gdata.contacts.data.Mileage,
        gdata.contacts.data.NickName,
        gdata.contacts.data.Occupation,
        gdata.contacts.data.Priority,
        gdata.contacts.data.Relation,
        gdata.contacts.data.Sensitivity,
        gdata.contacts.data.UserDefinedField,
        gdata.contacts.data.Website,
        gdata.contacts.data.HouseName,
        gdata.contacts.data.Street,
        gdata.contacts.data.POBox,
        gdata.contacts.data.Neighborhood,
        gdata.contacts.data.City,
        gdata.contacts.data.SubRegion,
        gdata.contacts.data.Region,
        gdata.contacts.data.PostalCode,
        gdata.contacts.data.Country,
        gdata.contacts.data.PersonEntry,
        gdata.contacts.data.Deleted,
        gdata.contacts.data.GroupMembershipInfo,
        gdata.contacts.data.ContactEntry,
        gdata.contacts.data.ContactsFeed,
        gdata.contacts.data.SystemGroup,
        gdata.contacts.data.GroupEntry,
        gdata.contacts.data.GroupsFeed,
        gdata.contacts.data.ProfileEntry,
        gdata.contacts.data.ProfilesFeed,
        gdata.opensearch.data.ItemsPerPage,
        gdata.opensearch.data.StartIndex,
        gdata.opensearch.data.TotalResults,
    ))


def suite():
  return conf.build_suite([DataSmokeTest])


if __name__ == '__main__':
  unittest.main()