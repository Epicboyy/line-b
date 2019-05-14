from ..ThriftService import *
import sys
import logging
from .ttypes import *

all_structs = []

class Iface(object):
    def getUserStatus(self, mid):
        """
        Parameters:
         - mid
        """
        pass

    def updateProfileAttributeForChannel(self, profileAttribute, value):
        """
        Parameters:
         - profileAttribute
         - value
        """
        pass

    def updateExtendedProfileAttribute(self, attr, extendedProfile):
        """
        Parameters:
         - attr
         - extendedProfile
        """
        pass

    def getAllSimpleChannelContacts(self, statusSticonFallbackDisabled):
        """
        Parameters:
         - statusSticonFallbackDisabled
        """
        pass

    def getUserIdentities(self):
        pass

    def markPaidCallAd(self, dialedNumber, language, disableCallerId):
        """
        Parameters:
         - dialedNumber
         - language
         - disableCallerId
        """
        pass

    def isGroupMember(self, groupId):
        """
        Parameters:
         - groupId
        """
        pass

    def getPhoneInfoFromPhoneNumber(self, region, phoneNumber):
        """
        Parameters:
         - region
         - phoneNumber
        """
        pass

    def redeemPaidCallVoucher(self, serial, language):
        """
        Parameters:
         - serial
         - language
        """
        pass

    def getPreferredDisplayName(self, mids):
        """
        Parameters:
         - mids
        """
        pass

    def getContactsForChannel(self, ids):
        """
        Parameters:
         - ids
        """
        pass

    def getCallCreditProducts(self, appStoreCode, pgCode, country, language):
        """
        Parameters:
         - appStoreCode
         - pgCode
         - country
         - language
        """
        pass

    def getCompactContacts(self, lastModifiedTimestamp):
        """
        Parameters:
         - lastModifiedTimestamp
        """
        pass

    def notifyNotiCenterEvent(self, event):
        """
        Parameters:
         - event
        """
        pass

    def isInContact(self, mid):
        """
        Parameters:
         - mid
        """
        pass

    def lookupGroupMembers(self, groupId, mids):
        """
        Parameters:
         - groupId
         - mids
        """
        pass

    def getRoomInformation(self, roomMid):
        """
        Parameters:
         - roomMid
        """
        pass

    def getGroupCall(self, chatMid):
        """
        Parameters:
         - chatMid
        """
        pass

    def isAllowSecondaryDeviceLogin(self):
        pass

    def getPrimaryClientForChannel(self):
        pass

    def createRoomWithBuddy(self, reqSeq, buddyMid, contactIds):
        """
        Parameters:
         - reqSeq
         - buddyMid
         - contactIds
        """
        pass

    def getDisplayName(self, mid):
        """
        Parameters:
         - mid
        """
        pass

    def getPaidCallMetadata(self, language):
        """
        Parameters:
         - language
        """
        pass

    def getMid(self):
        pass

    def getUserCountryForBilling(self, country, remoteIp):
        """
        Parameters:
         - country
         - remoteIp
        """
        pass

    def getFavoriteGroupIdsForChannel(self):
        pass

    def getPaidCallHistory(self, start, size, language):
        """
        Parameters:
         - start
         - size
         - language
        """
        pass

    def sendPinCodeOperation(self, verifier):
        """
        Parameters:
         - verifier
        """
        pass

    def inviteIntoGroupCall(self, chatMid, memberMids, mediaType):
        """
        Parameters:
         - chatMid
         - memberMids
         - mediaType
        """
        pass

    def getFriendMids(self):
        pass

    def getMetaProfile(self):
        pass

    def sendMessageForChannel(self, message):
        """
        Parameters:
         - message
        """
        pass

    def activeBuddySubscriberCount(self):
        pass

    def getCallCreditPurchaseHistory(self, request):
        """
        Parameters:
         - request
        """
        pass

    def isRoomMember(self, roomId):
        """
        Parameters:
         - roomId
        """
        pass

    def sendSystemOAMessage(self, message):
        """
        Parameters:
         - message
        """
        pass

    def acquirePaidCallRoute(self, paidCallType, dialedNumber, language, networkCode, disableCallerId, referer, adSessionId):
        """
        Parameters:
         - paidCallType
         - dialedNumber
         - language
         - networkCode
         - disableCallerId
         - referer
         - adSessionId
        """
        pass

    def getGroupsForChannel(self, groupIds):
        """
        Parameters:
         - groupIds
        """
        pass

    def getUserCreateTime(self):
        pass

    def registerChannelCP(self, cpId, registerPassword):
        """
        Parameters:
         - cpId
         - registerPassword
        """
        pass

    def reserveCallCreditPurchase(self, request):
        """
        Parameters:
         - request
        """
        pass

    def acquirePaidCallCurrencyExchangeRate(self, language):
        """
        Parameters:
         - language
        """
        pass

    def getRoomMemberMidsForAppPlatform(self, roomId):
        """
        Parameters:
         - roomId
        """
        pass

    def getPaidCallBalanceList(self, language):
        """
        Parameters:
         - language
        """
        pass

    def getPersonalInfos(self, requiredPersonalInfos):
        """
        Parameters:
         - requiredPersonalInfos
        """
        pass

    def getPrimaryClientsForChannel(self, userMids):
        """
        Parameters:
         - userMids
        """
        pass

    def addBuddyToContact(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getGroupMemberMidsForAppPlatform(self, groupId):
        """
        Parameters:
         - groupId
        """
        pass

    def getUserLanguage(self):
        pass

    def lookupPaidCall(self, dialedNumber, language, referer):
        """
        Parameters:
         - dialedNumber
         - language
         - referer
        """
        pass

    def getExtendedProfile(self):
        pass

    def getReverseCompactContacts(self, ids):
        """
        Parameters:
         - ids
        """
        pass

    def getPaidCallAdStatus(self):
        pass

    def findContactByUseridWithoutAbuseBlockForChannel(self, userid):
        """
        Parameters:
         - userid
        """
        pass

    def getGroupMemberMids(self, groupId):
        """
        Parameters:
         - groupId
        """
        pass

    def sendMessageWithoutRelationship(self, message):
        """
        Parameters:
         - message
        """
        pass

    def displayBuddySubscriberCountInBulk(self, mids):
        """
        Parameters:
         - mids
        """
        pass

    def lookupRoomMembers(self, roomId, mids):
        """
        Parameters:
         - roomId
         - mids
        """
        pass

    def getFavoriteMidsForChannel(self):
        pass

    def getAllContactIdsForChannel(self):
        pass

    def displayBuddySubscriberCount(self):
        pass

    def getProfileForChannel(self):
        pass

    def getUserTickets(self, userMids):
        """
        Parameters:
         - userMids
        """
        pass

    def getOAFriendMids(self):
        pass

    def searchPaidCallUserRate(self, countryCode, language):
        """
        Parameters:
         - countryCode
         - language
        """
        pass

    def getJoinedGroupIdsForChannel(self):
        pass

    def acquireGroupCallRoute(self, chatMid, mediaType):
        """
        Parameters:
         - chatMid
         - mediaType
        """
        pass

    def getUserMidsWhoAddedMe(self):
        pass

    def getIdentityCredential(self):
        pass

    def addOperationForChannel(self, opType, param1, param2, param3):
        """
        Parameters:
         - opType
         - param1
         - param2
         - param3
        """
        pass

    def getSimpleChannelContacts(self, ids, statusSticonFallbackDisabled):
        """
        Parameters:
         - ids
         - statusSticonFallbackDisabled
        """
        pass

    def getUserLastSentMessageTimeStamp(self, mid):
        """
        Parameters:
         - mid
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def getUserStatus(self, mid):
        """
        Parameters:
         - mid
        """
        self.send_getUserStatus(mid)
        return self.recv_getUserStatus()

    def send_getUserStatus(self, mid):
        self._oprot.writeMessageBegin('getUserStatus', TMessageType.CALL, self._seqid)
        args = getUserStatus_args()
        args.mid = mid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserStatus(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserStatus_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserStatus failed: unknown result")

    def updateProfileAttributeForChannel(self, profileAttribute, value):
        """
        Parameters:
         - profileAttribute
         - value
        """
        self.send_updateProfileAttributeForChannel(profileAttribute, value)
        self.recv_updateProfileAttributeForChannel()

    def send_updateProfileAttributeForChannel(self, profileAttribute, value):
        self._oprot.writeMessageBegin('updateProfileAttributeForChannel', TMessageType.CALL, self._seqid)
        args = updateProfileAttributeForChannel_args()
        args.profileAttribute = profileAttribute
        args.value = value
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateProfileAttributeForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateProfileAttributeForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def updateExtendedProfileAttribute(self, attr, extendedProfile):
        """
        Parameters:
         - attr
         - extendedProfile
        """
        self.send_updateExtendedProfileAttribute(attr, extendedProfile)
        self.recv_updateExtendedProfileAttribute()

    def send_updateExtendedProfileAttribute(self, attr, extendedProfile):
        self._oprot.writeMessageBegin('updateExtendedProfileAttribute', TMessageType.CALL, self._seqid)
        args = updateExtendedProfileAttribute_args()
        args.attr = attr
        args.extendedProfile = extendedProfile
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateExtendedProfileAttribute(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateExtendedProfileAttribute_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def getAllSimpleChannelContacts(self, statusSticonFallbackDisabled):
        """
        Parameters:
         - statusSticonFallbackDisabled
        """
        self.send_getAllSimpleChannelContacts(statusSticonFallbackDisabled)
        return self.recv_getAllSimpleChannelContacts()

    def send_getAllSimpleChannelContacts(self, statusSticonFallbackDisabled):
        self._oprot.writeMessageBegin('getAllSimpleChannelContacts', TMessageType.CALL, self._seqid)
        args = getAllSimpleChannelContacts_args()
        args.statusSticonFallbackDisabled = statusSticonFallbackDisabled
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getAllSimpleChannelContacts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getAllSimpleChannelContacts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getAllSimpleChannelContacts failed: unknown result")

    def getUserIdentities(self):
        self.send_getUserIdentities()
        return self.recv_getUserIdentities()

    def send_getUserIdentities(self):
        self._oprot.writeMessageBegin('getUserIdentities', TMessageType.CALL, self._seqid)
        args = getUserIdentities_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserIdentities(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserIdentities_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserIdentities failed: unknown result")

    def markPaidCallAd(self, dialedNumber, language, disableCallerId):
        """
        Parameters:
         - dialedNumber
         - language
         - disableCallerId
        """
        self.send_markPaidCallAd(dialedNumber, language, disableCallerId)
        return self.recv_markPaidCallAd()

    def send_markPaidCallAd(self, dialedNumber, language, disableCallerId):
        self._oprot.writeMessageBegin('markPaidCallAd', TMessageType.CALL, self._seqid)
        args = markPaidCallAd_args()
        args.dialedNumber = dialedNumber
        args.language = language
        args.disableCallerId = disableCallerId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_markPaidCallAd(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = markPaidCallAd_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "markPaidCallAd failed: unknown result")

    def isGroupMember(self, groupId):
        """
        Parameters:
         - groupId
        """
        self.send_isGroupMember(groupId)
        return self.recv_isGroupMember()

    def send_isGroupMember(self, groupId):
        self._oprot.writeMessageBegin('isGroupMember', TMessageType.CALL, self._seqid)
        args = isGroupMember_args()
        args.groupId = groupId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_isGroupMember(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = isGroupMember_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "isGroupMember failed: unknown result")

    def getPhoneInfoFromPhoneNumber(self, region, phoneNumber):
        """
        Parameters:
         - region
         - phoneNumber
        """
        self.send_getPhoneInfoFromPhoneNumber(region, phoneNumber)
        return self.recv_getPhoneInfoFromPhoneNumber()

    def send_getPhoneInfoFromPhoneNumber(self, region, phoneNumber):
        self._oprot.writeMessageBegin('getPhoneInfoFromPhoneNumber', TMessageType.CALL, self._seqid)
        args = getPhoneInfoFromPhoneNumber_args()
        args.region = region
        args.phoneNumber = phoneNumber
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPhoneInfoFromPhoneNumber(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPhoneInfoFromPhoneNumber_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPhoneInfoFromPhoneNumber failed: unknown result")

    def redeemPaidCallVoucher(self, serial, language):
        """
        Parameters:
         - serial
         - language
        """
        self.send_redeemPaidCallVoucher(serial, language)
        return self.recv_redeemPaidCallVoucher()

    def send_redeemPaidCallVoucher(self, serial, language):
        self._oprot.writeMessageBegin('redeemPaidCallVoucher', TMessageType.CALL, self._seqid)
        args = redeemPaidCallVoucher_args()
        args.serial = serial
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_redeemPaidCallVoucher(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = redeemPaidCallVoucher_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "redeemPaidCallVoucher failed: unknown result")

    def getPreferredDisplayName(self, mids):
        """
        Parameters:
         - mids
        """
        self.send_getPreferredDisplayName(mids)
        return self.recv_getPreferredDisplayName()

    def send_getPreferredDisplayName(self, mids):
        self._oprot.writeMessageBegin('getPreferredDisplayName', TMessageType.CALL, self._seqid)
        args = getPreferredDisplayName_args()
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPreferredDisplayName(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPreferredDisplayName_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPreferredDisplayName failed: unknown result")

    def getContactsForChannel(self, ids):
        """
        Parameters:
         - ids
        """
        self.send_getContactsForChannel(ids)
        return self.recv_getContactsForChannel()

    def send_getContactsForChannel(self, ids):
        self._oprot.writeMessageBegin('getContactsForChannel', TMessageType.CALL, self._seqid)
        args = getContactsForChannel_args()
        args.ids = ids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getContactsForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getContactsForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getContactsForChannel failed: unknown result")

    def getCallCreditProducts(self, appStoreCode, pgCode, country, language):
        """
        Parameters:
         - appStoreCode
         - pgCode
         - country
         - language
        """
        self.send_getCallCreditProducts(appStoreCode, pgCode, country, language)
        return self.recv_getCallCreditProducts()

    def send_getCallCreditProducts(self, appStoreCode, pgCode, country, language):
        self._oprot.writeMessageBegin('getCallCreditProducts', TMessageType.CALL, self._seqid)
        args = getCallCreditProducts_args()
        args.appStoreCode = appStoreCode
        args.pgCode = pgCode
        args.country = country
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCallCreditProducts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCallCreditProducts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCallCreditProducts failed: unknown result")

    def getCompactContacts(self, lastModifiedTimestamp):
        """
        Parameters:
         - lastModifiedTimestamp
        """
        self.send_getCompactContacts(lastModifiedTimestamp)
        return self.recv_getCompactContacts()

    def send_getCompactContacts(self, lastModifiedTimestamp):
        self._oprot.writeMessageBegin('getCompactContacts', TMessageType.CALL, self._seqid)
        args = getCompactContacts_args()
        args.lastModifiedTimestamp = lastModifiedTimestamp
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCompactContacts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCompactContacts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCompactContacts failed: unknown result")

    def notifyNotiCenterEvent(self, event):
        """
        Parameters:
         - event
        """
        self.send_notifyNotiCenterEvent(event)
        self.recv_notifyNotiCenterEvent()

    def send_notifyNotiCenterEvent(self, event):
        self._oprot.writeMessageBegin('notifyNotiCenterEvent', TMessageType.CALL, self._seqid)
        args = notifyNotiCenterEvent_args()
        args.event = event
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_notifyNotiCenterEvent(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyNotiCenterEvent_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def isInContact(self, mid):
        """
        Parameters:
         - mid
        """
        self.send_isInContact(mid)
        return self.recv_isInContact()

    def send_isInContact(self, mid):
        self._oprot.writeMessageBegin('isInContact', TMessageType.CALL, self._seqid)
        args = isInContact_args()
        args.mid = mid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_isInContact(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = isInContact_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "isInContact failed: unknown result")

    def lookupGroupMembers(self, groupId, mids):
        """
        Parameters:
         - groupId
         - mids
        """
        self.send_lookupGroupMembers(groupId, mids)
        return self.recv_lookupGroupMembers()

    def send_lookupGroupMembers(self, groupId, mids):
        self._oprot.writeMessageBegin('lookupGroupMembers', TMessageType.CALL, self._seqid)
        args = lookupGroupMembers_args()
        args.groupId = groupId
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_lookupGroupMembers(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = lookupGroupMembers_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "lookupGroupMembers failed: unknown result")

    def getRoomInformation(self, roomMid):
        """
        Parameters:
         - roomMid
        """
        self.send_getRoomInformation(roomMid)
        return self.recv_getRoomInformation()

    def send_getRoomInformation(self, roomMid):
        self._oprot.writeMessageBegin('getRoomInformation', TMessageType.CALL, self._seqid)
        args = getRoomInformation_args()
        args.roomMid = roomMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getRoomInformation(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getRoomInformation_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getRoomInformation failed: unknown result")

    def getGroupCall(self, chatMid):
        """
        Parameters:
         - chatMid
        """
        self.send_getGroupCall(chatMid)
        return self.recv_getGroupCall()

    def send_getGroupCall(self, chatMid):
        self._oprot.writeMessageBegin('getGroupCall', TMessageType.CALL, self._seqid)
        args = getGroupCall_args()
        args.chatMid = chatMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getGroupCall(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getGroupCall_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getGroupCall failed: unknown result")

    def isAllowSecondaryDeviceLogin(self):
        self.send_isAllowSecondaryDeviceLogin()
        return self.recv_isAllowSecondaryDeviceLogin()

    def send_isAllowSecondaryDeviceLogin(self):
        self._oprot.writeMessageBegin('isAllowSecondaryDeviceLogin', TMessageType.CALL, self._seqid)
        args = isAllowSecondaryDeviceLogin_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_isAllowSecondaryDeviceLogin(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = isAllowSecondaryDeviceLogin_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "isAllowSecondaryDeviceLogin failed: unknown result")

    def getPrimaryClientForChannel(self):
        self.send_getPrimaryClientForChannel()
        return self.recv_getPrimaryClientForChannel()

    def send_getPrimaryClientForChannel(self):
        self._oprot.writeMessageBegin('getPrimaryClientForChannel', TMessageType.CALL, self._seqid)
        args = getPrimaryClientForChannel_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPrimaryClientForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPrimaryClientForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPrimaryClientForChannel failed: unknown result")

    def createRoomWithBuddy(self, reqSeq, buddyMid, contactIds):
        """
        Parameters:
         - reqSeq
         - buddyMid
         - contactIds
        """
        self.send_createRoomWithBuddy(reqSeq, buddyMid, contactIds)
        return self.recv_createRoomWithBuddy()

    def send_createRoomWithBuddy(self, reqSeq, buddyMid, contactIds):
        self._oprot.writeMessageBegin('createRoomWithBuddy', TMessageType.CALL, self._seqid)
        args = createRoomWithBuddy_args()
        args.reqSeq = reqSeq
        args.buddyMid = buddyMid
        args.contactIds = contactIds
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_createRoomWithBuddy(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = createRoomWithBuddy_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "createRoomWithBuddy failed: unknown result")

    def getDisplayName(self, mid):
        """
        Parameters:
         - mid
        """
        self.send_getDisplayName(mid)
        return self.recv_getDisplayName()

    def send_getDisplayName(self, mid):
        self._oprot.writeMessageBegin('getDisplayName', TMessageType.CALL, self._seqid)
        args = getDisplayName_args()
        args.mid = mid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getDisplayName(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getDisplayName_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getDisplayName failed: unknown result")

    def getPaidCallMetadata(self, language):
        """
        Parameters:
         - language
        """
        self.send_getPaidCallMetadata(language)
        return self.recv_getPaidCallMetadata()

    def send_getPaidCallMetadata(self, language):
        self._oprot.writeMessageBegin('getPaidCallMetadata', TMessageType.CALL, self._seqid)
        args = getPaidCallMetadata_args()
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPaidCallMetadata(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPaidCallMetadata_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPaidCallMetadata failed: unknown result")

    def getMid(self):
        self.send_getMid()
        return self.recv_getMid()

    def send_getMid(self):
        self._oprot.writeMessageBegin('getMid', TMessageType.CALL, self._seqid)
        args = getMid_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getMid(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getMid_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getMid failed: unknown result")

    def getUserCountryForBilling(self, country, remoteIp):
        """
        Parameters:
         - country
         - remoteIp
        """
        self.send_getUserCountryForBilling(country, remoteIp)
        return self.recv_getUserCountryForBilling()

    def send_getUserCountryForBilling(self, country, remoteIp):
        self._oprot.writeMessageBegin('getUserCountryForBilling', TMessageType.CALL, self._seqid)
        args = getUserCountryForBilling_args()
        args.country = country
        args.remoteIp = remoteIp
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserCountryForBilling(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserCountryForBilling_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserCountryForBilling failed: unknown result")

    def getFavoriteGroupIdsForChannel(self):
        self.send_getFavoriteGroupIdsForChannel()
        return self.recv_getFavoriteGroupIdsForChannel()

    def send_getFavoriteGroupIdsForChannel(self):
        self._oprot.writeMessageBegin('getFavoriteGroupIdsForChannel', TMessageType.CALL, self._seqid)
        args = getFavoriteGroupIdsForChannel_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getFavoriteGroupIdsForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getFavoriteGroupIdsForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getFavoriteGroupIdsForChannel failed: unknown result")

    def getPaidCallHistory(self, start, size, language):
        """
        Parameters:
         - start
         - size
         - language
        """
        self.send_getPaidCallHistory(start, size, language)
        return self.recv_getPaidCallHistory()

    def send_getPaidCallHistory(self, start, size, language):
        self._oprot.writeMessageBegin('getPaidCallHistory', TMessageType.CALL, self._seqid)
        args = getPaidCallHistory_args()
        args.start = start
        args.size = size
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPaidCallHistory(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPaidCallHistory_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPaidCallHistory failed: unknown result")

    def sendPinCodeOperation(self, verifier):
        """
        Parameters:
         - verifier
        """
        self.send_sendPinCodeOperation(verifier)
        self.recv_sendPinCodeOperation()

    def send_sendPinCodeOperation(self, verifier):
        self._oprot.writeMessageBegin('sendPinCodeOperation', TMessageType.CALL, self._seqid)
        args = sendPinCodeOperation_args()
        args.verifier = verifier
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendPinCodeOperation(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendPinCodeOperation_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def inviteIntoGroupCall(self, chatMid, memberMids, mediaType):
        """
        Parameters:
         - chatMid
         - memberMids
         - mediaType
        """
        self.send_inviteIntoGroupCall(chatMid, memberMids, mediaType)
        self.recv_inviteIntoGroupCall()

    def send_inviteIntoGroupCall(self, chatMid, memberMids, mediaType):
        self._oprot.writeMessageBegin('inviteIntoGroupCall', TMessageType.CALL, self._seqid)
        args = inviteIntoGroupCall_args()
        args.chatMid = chatMid
        args.memberMids = memberMids
        args.mediaType = mediaType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_inviteIntoGroupCall(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = inviteIntoGroupCall_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def getFriendMids(self):
        self.send_getFriendMids()
        return self.recv_getFriendMids()

    def send_getFriendMids(self):
        self._oprot.writeMessageBegin('getFriendMids', TMessageType.CALL, self._seqid)
        args = getFriendMids_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getFriendMids(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getFriendMids_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getFriendMids failed: unknown result")

    def getMetaProfile(self):
        self.send_getMetaProfile()
        return self.recv_getMetaProfile()

    def send_getMetaProfile(self):
        self._oprot.writeMessageBegin('getMetaProfile', TMessageType.CALL, self._seqid)
        args = getMetaProfile_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getMetaProfile(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getMetaProfile_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getMetaProfile failed: unknown result")

    def sendMessageForChannel(self, message):
        """
        Parameters:
         - message
        """
        self.send_sendMessageForChannel(message)
        return self.recv_sendMessageForChannel()

    def send_sendMessageForChannel(self, message):
        self._oprot.writeMessageBegin('sendMessageForChannel', TMessageType.CALL, self._seqid)
        args = sendMessageForChannel_args()
        args.message = message
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendMessageForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendMessageForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendMessageForChannel failed: unknown result")

    def activeBuddySubscriberCount(self):
        self.send_activeBuddySubscriberCount()
        return self.recv_activeBuddySubscriberCount()

    def send_activeBuddySubscriberCount(self):
        self._oprot.writeMessageBegin('activeBuddySubscriberCount', TMessageType.CALL, self._seqid)
        args = activeBuddySubscriberCount_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_activeBuddySubscriberCount(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = activeBuddySubscriberCount_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "activeBuddySubscriberCount failed: unknown result")

    def getCallCreditPurchaseHistory(self, request):
        """
        Parameters:
         - request
        """
        self.send_getCallCreditPurchaseHistory(request)
        return self.recv_getCallCreditPurchaseHistory()

    def send_getCallCreditPurchaseHistory(self, request):
        self._oprot.writeMessageBegin('getCallCreditPurchaseHistory', TMessageType.CALL, self._seqid)
        args = getCallCreditPurchaseHistory_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCallCreditPurchaseHistory(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCallCreditPurchaseHistory_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCallCreditPurchaseHistory failed: unknown result")

    def isRoomMember(self, roomId):
        """
        Parameters:
         - roomId
        """
        self.send_isRoomMember(roomId)
        return self.recv_isRoomMember()

    def send_isRoomMember(self, roomId):
        self._oprot.writeMessageBegin('isRoomMember', TMessageType.CALL, self._seqid)
        args = isRoomMember_args()
        args.roomId = roomId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_isRoomMember(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = isRoomMember_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "isRoomMember failed: unknown result")

    def sendSystemOAMessage(self, message):
        """
        Parameters:
         - message
        """
        self.send_sendSystemOAMessage(message)
        return self.recv_sendSystemOAMessage()

    def send_sendSystemOAMessage(self, message):
        self._oprot.writeMessageBegin('sendSystemOAMessage', TMessageType.CALL, self._seqid)
        args = sendSystemOAMessage_args()
        args.message = message
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendSystemOAMessage(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendSystemOAMessage_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendSystemOAMessage failed: unknown result")

    def acquirePaidCallRoute(self, paidCallType, dialedNumber, language, networkCode, disableCallerId, referer, adSessionId):
        """
        Parameters:
         - paidCallType
         - dialedNumber
         - language
         - networkCode
         - disableCallerId
         - referer
         - adSessionId
        """
        self.send_acquirePaidCallRoute(paidCallType, dialedNumber, language, networkCode, disableCallerId, referer, adSessionId)
        return self.recv_acquirePaidCallRoute()

    def send_acquirePaidCallRoute(self, paidCallType, dialedNumber, language, networkCode, disableCallerId, referer, adSessionId):
        self._oprot.writeMessageBegin('acquirePaidCallRoute', TMessageType.CALL, self._seqid)
        args = acquirePaidCallRoute_args()
        args.paidCallType = paidCallType
        args.dialedNumber = dialedNumber
        args.language = language
        args.networkCode = networkCode
        args.disableCallerId = disableCallerId
        args.referer = referer
        args.adSessionId = adSessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_acquirePaidCallRoute(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = acquirePaidCallRoute_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "acquirePaidCallRoute failed: unknown result")

    def getGroupsForChannel(self, groupIds):
        """
        Parameters:
         - groupIds
        """
        self.send_getGroupsForChannel(groupIds)
        return self.recv_getGroupsForChannel()

    def send_getGroupsForChannel(self, groupIds):
        self._oprot.writeMessageBegin('getGroupsForChannel', TMessageType.CALL, self._seqid)
        args = getGroupsForChannel_args()
        args.groupIds = groupIds
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getGroupsForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getGroupsForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getGroupsForChannel failed: unknown result")

    def getUserCreateTime(self):
        self.send_getUserCreateTime()
        return self.recv_getUserCreateTime()

    def send_getUserCreateTime(self):
        self._oprot.writeMessageBegin('getUserCreateTime', TMessageType.CALL, self._seqid)
        args = getUserCreateTime_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserCreateTime(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserCreateTime_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserCreateTime failed: unknown result")

    def registerChannelCP(self, cpId, registerPassword):
        """
        Parameters:
         - cpId
         - registerPassword
        """
        self.send_registerChannelCP(cpId, registerPassword)
        return self.recv_registerChannelCP()

    def send_registerChannelCP(self, cpId, registerPassword):
        self._oprot.writeMessageBegin('registerChannelCP', TMessageType.CALL, self._seqid)
        args = registerChannelCP_args()
        args.cpId = cpId
        args.registerPassword = registerPassword
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_registerChannelCP(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = registerChannelCP_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "registerChannelCP failed: unknown result")

    def reserveCallCreditPurchase(self, request):
        """
        Parameters:
         - request
        """
        self.send_reserveCallCreditPurchase(request)
        return self.recv_reserveCallCreditPurchase()

    def send_reserveCallCreditPurchase(self, request):
        self._oprot.writeMessageBegin('reserveCallCreditPurchase', TMessageType.CALL, self._seqid)
        args = reserveCallCreditPurchase_args()
        args.request = request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_reserveCallCreditPurchase(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = reserveCallCreditPurchase_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "reserveCallCreditPurchase failed: unknown result")

    def acquirePaidCallCurrencyExchangeRate(self, language):
        """
        Parameters:
         - language
        """
        self.send_acquirePaidCallCurrencyExchangeRate(language)
        return self.recv_acquirePaidCallCurrencyExchangeRate()

    def send_acquirePaidCallCurrencyExchangeRate(self, language):
        self._oprot.writeMessageBegin('acquirePaidCallCurrencyExchangeRate', TMessageType.CALL, self._seqid)
        args = acquirePaidCallCurrencyExchangeRate_args()
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_acquirePaidCallCurrencyExchangeRate(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = acquirePaidCallCurrencyExchangeRate_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "acquirePaidCallCurrencyExchangeRate failed: unknown result")

    def getRoomMemberMidsForAppPlatform(self, roomId):
        """
        Parameters:
         - roomId
        """
        self.send_getRoomMemberMidsForAppPlatform(roomId)
        return self.recv_getRoomMemberMidsForAppPlatform()

    def send_getRoomMemberMidsForAppPlatform(self, roomId):
        self._oprot.writeMessageBegin('getRoomMemberMidsForAppPlatform', TMessageType.CALL, self._seqid)
        args = getRoomMemberMidsForAppPlatform_args()
        args.roomId = roomId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getRoomMemberMidsForAppPlatform(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getRoomMemberMidsForAppPlatform_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getRoomMemberMidsForAppPlatform failed: unknown result")

    def getPaidCallBalanceList(self, language):
        """
        Parameters:
         - language
        """
        self.send_getPaidCallBalanceList(language)
        return self.recv_getPaidCallBalanceList()

    def send_getPaidCallBalanceList(self, language):
        self._oprot.writeMessageBegin('getPaidCallBalanceList', TMessageType.CALL, self._seqid)
        args = getPaidCallBalanceList_args()
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPaidCallBalanceList(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPaidCallBalanceList_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPaidCallBalanceList failed: unknown result")

    def getPersonalInfos(self, requiredPersonalInfos):
        """
        Parameters:
         - requiredPersonalInfos
        """
        self.send_getPersonalInfos(requiredPersonalInfos)
        return self.recv_getPersonalInfos()

    def send_getPersonalInfos(self, requiredPersonalInfos):
        self._oprot.writeMessageBegin('getPersonalInfos', TMessageType.CALL, self._seqid)
        args = getPersonalInfos_args()
        args.requiredPersonalInfos = requiredPersonalInfos
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPersonalInfos(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPersonalInfos_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPersonalInfos failed: unknown result")

    def getPrimaryClientsForChannel(self, userMids):
        """
        Parameters:
         - userMids
        """
        self.send_getPrimaryClientsForChannel(userMids)
        return self.recv_getPrimaryClientsForChannel()

    def send_getPrimaryClientsForChannel(self, userMids):
        self._oprot.writeMessageBegin('getPrimaryClientsForChannel', TMessageType.CALL, self._seqid)
        args = getPrimaryClientsForChannel_args()
        args.userMids = userMids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPrimaryClientsForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPrimaryClientsForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPrimaryClientsForChannel failed: unknown result")

    def addBuddyToContact(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_addBuddyToContact(buddyMid)
        return self.recv_addBuddyToContact()

    def send_addBuddyToContact(self, buddyMid):
        self._oprot.writeMessageBegin('addBuddyToContact', TMessageType.CALL, self._seqid)
        args = addBuddyToContact_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_addBuddyToContact(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = addBuddyToContact_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "addBuddyToContact failed: unknown result")

    def getGroupMemberMidsForAppPlatform(self, groupId):
        """
        Parameters:
         - groupId
        """
        self.send_getGroupMemberMidsForAppPlatform(groupId)
        return self.recv_getGroupMemberMidsForAppPlatform()

    def send_getGroupMemberMidsForAppPlatform(self, groupId):
        self._oprot.writeMessageBegin('getGroupMemberMidsForAppPlatform', TMessageType.CALL, self._seqid)
        args = getGroupMemberMidsForAppPlatform_args()
        args.groupId = groupId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getGroupMemberMidsForAppPlatform(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getGroupMemberMidsForAppPlatform_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getGroupMemberMidsForAppPlatform failed: unknown result")

    def getUserLanguage(self):
        self.send_getUserLanguage()
        return self.recv_getUserLanguage()

    def send_getUserLanguage(self):
        self._oprot.writeMessageBegin('getUserLanguage', TMessageType.CALL, self._seqid)
        args = getUserLanguage_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserLanguage(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserLanguage_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserLanguage failed: unknown result")

    def lookupPaidCall(self, dialedNumber, language, referer):
        """
        Parameters:
         - dialedNumber
         - language
         - referer
        """
        self.send_lookupPaidCall(dialedNumber, language, referer)
        return self.recv_lookupPaidCall()

    def send_lookupPaidCall(self, dialedNumber, language, referer):
        self._oprot.writeMessageBegin('lookupPaidCall', TMessageType.CALL, self._seqid)
        args = lookupPaidCall_args()
        args.dialedNumber = dialedNumber
        args.language = language
        args.referer = referer
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_lookupPaidCall(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = lookupPaidCall_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "lookupPaidCall failed: unknown result")

    def getExtendedProfile(self):
        self.send_getExtendedProfile()
        return self.recv_getExtendedProfile()

    def send_getExtendedProfile(self):
        self._oprot.writeMessageBegin('getExtendedProfile', TMessageType.CALL, self._seqid)
        args = getExtendedProfile_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getExtendedProfile(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getExtendedProfile_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getExtendedProfile failed: unknown result")

    def getReverseCompactContacts(self, ids):
        """
        Parameters:
         - ids
        """
        self.send_getReverseCompactContacts(ids)
        return self.recv_getReverseCompactContacts()

    def send_getReverseCompactContacts(self, ids):
        self._oprot.writeMessageBegin('getReverseCompactContacts', TMessageType.CALL, self._seqid)
        args = getReverseCompactContacts_args()
        args.ids = ids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getReverseCompactContacts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getReverseCompactContacts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getReverseCompactContacts failed: unknown result")

    def getPaidCallAdStatus(self):
        self.send_getPaidCallAdStatus()
        return self.recv_getPaidCallAdStatus()

    def send_getPaidCallAdStatus(self):
        self._oprot.writeMessageBegin('getPaidCallAdStatus', TMessageType.CALL, self._seqid)
        args = getPaidCallAdStatus_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPaidCallAdStatus(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPaidCallAdStatus_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPaidCallAdStatus failed: unknown result")

    def findContactByUseridWithoutAbuseBlockForChannel(self, userid):
        """
        Parameters:
         - userid
        """
        self.send_findContactByUseridWithoutAbuseBlockForChannel(userid)
        return self.recv_findContactByUseridWithoutAbuseBlockForChannel()

    def send_findContactByUseridWithoutAbuseBlockForChannel(self, userid):
        self._oprot.writeMessageBegin('findContactByUseridWithoutAbuseBlockForChannel', TMessageType.CALL, self._seqid)
        args = findContactByUseridWithoutAbuseBlockForChannel_args()
        args.userid = userid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_findContactByUseridWithoutAbuseBlockForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = findContactByUseridWithoutAbuseBlockForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "findContactByUseridWithoutAbuseBlockForChannel failed: unknown result")

    def getGroupMemberMids(self, groupId):
        """
        Parameters:
         - groupId
        """
        self.send_getGroupMemberMids(groupId)
        return self.recv_getGroupMemberMids()

    def send_getGroupMemberMids(self, groupId):
        self._oprot.writeMessageBegin('getGroupMemberMids', TMessageType.CALL, self._seqid)
        args = getGroupMemberMids_args()
        args.groupId = groupId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getGroupMemberMids(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getGroupMemberMids_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getGroupMemberMids failed: unknown result")

    def sendMessageWithoutRelationship(self, message):
        """
        Parameters:
         - message
        """
        self.send_sendMessageWithoutRelationship(message)
        return self.recv_sendMessageWithoutRelationship()

    def send_sendMessageWithoutRelationship(self, message):
        self._oprot.writeMessageBegin('sendMessageWithoutRelationship', TMessageType.CALL, self._seqid)
        args = sendMessageWithoutRelationship_args()
        args.message = message
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendMessageWithoutRelationship(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendMessageWithoutRelationship_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendMessageWithoutRelationship failed: unknown result")

    def displayBuddySubscriberCountInBulk(self, mids):
        """
        Parameters:
         - mids
        """
        self.send_displayBuddySubscriberCountInBulk(mids)
        return self.recv_displayBuddySubscriberCountInBulk()

    def send_displayBuddySubscriberCountInBulk(self, mids):
        self._oprot.writeMessageBegin('displayBuddySubscriberCountInBulk', TMessageType.CALL, self._seqid)
        args = displayBuddySubscriberCountInBulk_args()
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_displayBuddySubscriberCountInBulk(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = displayBuddySubscriberCountInBulk_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "displayBuddySubscriberCountInBulk failed: unknown result")

    def lookupRoomMembers(self, roomId, mids):
        """
        Parameters:
         - roomId
         - mids
        """
        self.send_lookupRoomMembers(roomId, mids)
        return self.recv_lookupRoomMembers()

    def send_lookupRoomMembers(self, roomId, mids):
        self._oprot.writeMessageBegin('lookupRoomMembers', TMessageType.CALL, self._seqid)
        args = lookupRoomMembers_args()
        args.roomId = roomId
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_lookupRoomMembers(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = lookupRoomMembers_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "lookupRoomMembers failed: unknown result")

    def getFavoriteMidsForChannel(self):
        self.send_getFavoriteMidsForChannel()
        return self.recv_getFavoriteMidsForChannel()

    def send_getFavoriteMidsForChannel(self):
        self._oprot.writeMessageBegin('getFavoriteMidsForChannel', TMessageType.CALL, self._seqid)
        args = getFavoriteMidsForChannel_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getFavoriteMidsForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getFavoriteMidsForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getFavoriteMidsForChannel failed: unknown result")

    def getAllContactIdsForChannel(self):
        self.send_getAllContactIdsForChannel()
        return self.recv_getAllContactIdsForChannel()

    def send_getAllContactIdsForChannel(self):
        self._oprot.writeMessageBegin('getAllContactIdsForChannel', TMessageType.CALL, self._seqid)
        args = getAllContactIdsForChannel_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getAllContactIdsForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getAllContactIdsForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getAllContactIdsForChannel failed: unknown result")

    def displayBuddySubscriberCount(self):
        self.send_displayBuddySubscriberCount()
        return self.recv_displayBuddySubscriberCount()

    def send_displayBuddySubscriberCount(self):
        self._oprot.writeMessageBegin('displayBuddySubscriberCount', TMessageType.CALL, self._seqid)
        args = displayBuddySubscriberCount_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_displayBuddySubscriberCount(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = displayBuddySubscriberCount_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "displayBuddySubscriberCount failed: unknown result")

    def getProfileForChannel(self):
        self.send_getProfileForChannel()
        return self.recv_getProfileForChannel()

    def send_getProfileForChannel(self):
        self._oprot.writeMessageBegin('getProfileForChannel', TMessageType.CALL, self._seqid)
        args = getProfileForChannel_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getProfileForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getProfileForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getProfileForChannel failed: unknown result")

    def getUserTickets(self, userMids):
        """
        Parameters:
         - userMids
        """
        self.send_getUserTickets(userMids)
        return self.recv_getUserTickets()

    def send_getUserTickets(self, userMids):
        self._oprot.writeMessageBegin('getUserTickets', TMessageType.CALL, self._seqid)
        args = getUserTickets_args()
        args.userMids = userMids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserTickets(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserTickets_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserTickets failed: unknown result")

    def getOAFriendMids(self):
        self.send_getOAFriendMids()
        return self.recv_getOAFriendMids()

    def send_getOAFriendMids(self):
        self._oprot.writeMessageBegin('getOAFriendMids', TMessageType.CALL, self._seqid)
        args = getOAFriendMids_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getOAFriendMids(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getOAFriendMids_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getOAFriendMids failed: unknown result")

    def searchPaidCallUserRate(self, countryCode, language):
        """
        Parameters:
         - countryCode
         - language
        """
        self.send_searchPaidCallUserRate(countryCode, language)
        return self.recv_searchPaidCallUserRate()

    def send_searchPaidCallUserRate(self, countryCode, language):
        self._oprot.writeMessageBegin('searchPaidCallUserRate', TMessageType.CALL, self._seqid)
        args = searchPaidCallUserRate_args()
        args.countryCode = countryCode
        args.language = language
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_searchPaidCallUserRate(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = searchPaidCallUserRate_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "searchPaidCallUserRate failed: unknown result")

    def getJoinedGroupIdsForChannel(self):
        self.send_getJoinedGroupIdsForChannel()
        return self.recv_getJoinedGroupIdsForChannel()

    def send_getJoinedGroupIdsForChannel(self):
        self._oprot.writeMessageBegin('getJoinedGroupIdsForChannel', TMessageType.CALL, self._seqid)
        args = getJoinedGroupIdsForChannel_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getJoinedGroupIdsForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getJoinedGroupIdsForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getJoinedGroupIdsForChannel failed: unknown result")

    def acquireGroupCallRoute(self, chatMid, mediaType):
        """
        Parameters:
         - chatMid
         - mediaType
        """
        self.send_acquireGroupCallRoute(chatMid, mediaType)
        return self.recv_acquireGroupCallRoute()

    def send_acquireGroupCallRoute(self, chatMid, mediaType):
        self._oprot.writeMessageBegin('acquireGroupCallRoute', TMessageType.CALL, self._seqid)
        args = acquireGroupCallRoute_args()
        args.chatMid = chatMid
        args.mediaType = mediaType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_acquireGroupCallRoute(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = acquireGroupCallRoute_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "acquireGroupCallRoute failed: unknown result")

    def getUserMidsWhoAddedMe(self):
        self.send_getUserMidsWhoAddedMe()
        return self.recv_getUserMidsWhoAddedMe()

    def send_getUserMidsWhoAddedMe(self):
        self._oprot.writeMessageBegin('getUserMidsWhoAddedMe', TMessageType.CALL, self._seqid)
        args = getUserMidsWhoAddedMe_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserMidsWhoAddedMe(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserMidsWhoAddedMe_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserMidsWhoAddedMe failed: unknown result")

    def getIdentityCredential(self):
        self.send_getIdentityCredential()
        return self.recv_getIdentityCredential()

    def send_getIdentityCredential(self):
        self._oprot.writeMessageBegin('getIdentityCredential', TMessageType.CALL, self._seqid)
        args = getIdentityCredential_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getIdentityCredential(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getIdentityCredential_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getIdentityCredential failed: unknown result")

    def addOperationForChannel(self, opType, param1, param2, param3):
        """
        Parameters:
         - opType
         - param1
         - param2
         - param3
        """
        self.send_addOperationForChannel(opType, param1, param2, param3)
        self.recv_addOperationForChannel()

    def send_addOperationForChannel(self, opType, param1, param2, param3):
        self._oprot.writeMessageBegin('addOperationForChannel', TMessageType.CALL, self._seqid)
        args = addOperationForChannel_args()
        args.opType = opType
        args.param1 = param1
        args.param2 = param2
        args.param3 = param3
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_addOperationForChannel(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = addOperationForChannel_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def getSimpleChannelContacts(self, ids, statusSticonFallbackDisabled):
        """
        Parameters:
         - ids
         - statusSticonFallbackDisabled
        """
        self.send_getSimpleChannelContacts(ids, statusSticonFallbackDisabled)
        return self.recv_getSimpleChannelContacts()

    def send_getSimpleChannelContacts(self, ids, statusSticonFallbackDisabled):
        self._oprot.writeMessageBegin('getSimpleChannelContacts', TMessageType.CALL, self._seqid)
        args = getSimpleChannelContacts_args()
        args.ids = ids
        args.statusSticonFallbackDisabled = statusSticonFallbackDisabled
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getSimpleChannelContacts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getSimpleChannelContacts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getSimpleChannelContacts failed: unknown result")

    def getUserLastSentMessageTimeStamp(self, mid):
        """
        Parameters:
         - mid
        """
        self.send_getUserLastSentMessageTimeStamp(mid)
        return self.recv_getUserLastSentMessageTimeStamp()

    def send_getUserLastSentMessageTimeStamp(self, mid):
        self._oprot.writeMessageBegin('getUserLastSentMessageTimeStamp', TMessageType.CALL, self._seqid)
        args = getUserLastSentMessageTimeStamp_args()
        args.mid = mid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUserLastSentMessageTimeStamp(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUserLastSentMessageTimeStamp_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUserLastSentMessageTimeStamp failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["getUserStatus"] = Processor.process_getUserStatus
        self._processMap["updateProfileAttributeForChannel"] = Processor.process_updateProfileAttributeForChannel
        self._processMap["updateExtendedProfileAttribute"] = Processor.process_updateExtendedProfileAttribute
        self._processMap["getAllSimpleChannelContacts"] = Processor.process_getAllSimpleChannelContacts
        self._processMap["getUserIdentities"] = Processor.process_getUserIdentities
        self._processMap["markPaidCallAd"] = Processor.process_markPaidCallAd
        self._processMap["isGroupMember"] = Processor.process_isGroupMember
        self._processMap["getPhoneInfoFromPhoneNumber"] = Processor.process_getPhoneInfoFromPhoneNumber
        self._processMap["redeemPaidCallVoucher"] = Processor.process_redeemPaidCallVoucher
        self._processMap["getPreferredDisplayName"] = Processor.process_getPreferredDisplayName
        self._processMap["getContactsForChannel"] = Processor.process_getContactsForChannel
        self._processMap["getCallCreditProducts"] = Processor.process_getCallCreditProducts
        self._processMap["getCompactContacts"] = Processor.process_getCompactContacts
        self._processMap["notifyNotiCenterEvent"] = Processor.process_notifyNotiCenterEvent
        self._processMap["isInContact"] = Processor.process_isInContact
        self._processMap["lookupGroupMembers"] = Processor.process_lookupGroupMembers
        self._processMap["getRoomInformation"] = Processor.process_getRoomInformation
        self._processMap["getGroupCall"] = Processor.process_getGroupCall
        self._processMap["isAllowSecondaryDeviceLogin"] = Processor.process_isAllowSecondaryDeviceLogin
        self._processMap["getPrimaryClientForChannel"] = Processor.process_getPrimaryClientForChannel
        self._processMap["createRoomWithBuddy"] = Processor.process_createRoomWithBuddy
        self._processMap["getDisplayName"] = Processor.process_getDisplayName
        self._processMap["getPaidCallMetadata"] = Processor.process_getPaidCallMetadata
        self._processMap["getMid"] = Processor.process_getMid
        self._processMap["getUserCountryForBilling"] = Processor.process_getUserCountryForBilling
        self._processMap["getFavoriteGroupIdsForChannel"] = Processor.process_getFavoriteGroupIdsForChannel
        self._processMap["getPaidCallHistory"] = Processor.process_getPaidCallHistory
        self._processMap["sendPinCodeOperation"] = Processor.process_sendPinCodeOperation
        self._processMap["inviteIntoGroupCall"] = Processor.process_inviteIntoGroupCall
        self._processMap["getFriendMids"] = Processor.process_getFriendMids
        self._processMap["getMetaProfile"] = Processor.process_getMetaProfile
        self._processMap["sendMessageForChannel"] = Processor.process_sendMessageForChannel
        self._processMap["activeBuddySubscriberCount"] = Processor.process_activeBuddySubscriberCount
        self._processMap["getCallCreditPurchaseHistory"] = Processor.process_getCallCreditPurchaseHistory
        self._processMap["isRoomMember"] = Processor.process_isRoomMember
        self._processMap["sendSystemOAMessage"] = Processor.process_sendSystemOAMessage
        self._processMap["acquirePaidCallRoute"] = Processor.process_acquirePaidCallRoute
        self._processMap["getGroupsForChannel"] = Processor.process_getGroupsForChannel
        self._processMap["getUserCreateTime"] = Processor.process_getUserCreateTime
        self._processMap["registerChannelCP"] = Processor.process_registerChannelCP
        self._processMap["reserveCallCreditPurchase"] = Processor.process_reserveCallCreditPurchase
        self._processMap["acquirePaidCallCurrencyExchangeRate"] = Processor.process_acquirePaidCallCurrencyExchangeRate
        self._processMap["getRoomMemberMidsForAppPlatform"] = Processor.process_getRoomMemberMidsForAppPlatform
        self._processMap["getPaidCallBalanceList"] = Processor.process_getPaidCallBalanceList
        self._processMap["getPersonalInfos"] = Processor.process_getPersonalInfos
        self._processMap["getPrimaryClientsForChannel"] = Processor.process_getPrimaryClientsForChannel
        self._processMap["addBuddyToContact"] = Processor.process_addBuddyToContact
        self._processMap["getGroupMemberMidsForAppPlatform"] = Processor.process_getGroupMemberMidsForAppPlatform
        self._processMap["getUserLanguage"] = Processor.process_getUserLanguage
        self._processMap["lookupPaidCall"] = Processor.process_lookupPaidCall
        self._processMap["getExtendedProfile"] = Processor.process_getExtendedProfile
        self._processMap["getReverseCompactContacts"] = Processor.process_getReverseCompactContacts
        self._processMap["getPaidCallAdStatus"] = Processor.process_getPaidCallAdStatus
        self._processMap["findContactByUseridWithoutAbuseBlockForChannel"] = Processor.process_findContactByUseridWithoutAbuseBlockForChannel
        self._processMap["getGroupMemberMids"] = Processor.process_getGroupMemberMids
        self._processMap["sendMessageWithoutRelationship"] = Processor.process_sendMessageWithoutRelationship
        self._processMap["displayBuddySubscriberCountInBulk"] = Processor.process_displayBuddySubscriberCountInBulk
        self._processMap["lookupRoomMembers"] = Processor.process_lookupRoomMembers
        self._processMap["getFavoriteMidsForChannel"] = Processor.process_getFavoriteMidsForChannel
        self._processMap["getAllContactIdsForChannel"] = Processor.process_getAllContactIdsForChannel
        self._processMap["displayBuddySubscriberCount"] = Processor.process_displayBuddySubscriberCount
        self._processMap["getProfileForChannel"] = Processor.process_getProfileForChannel
        self._processMap["getUserTickets"] = Processor.process_getUserTickets
        self._processMap["getOAFriendMids"] = Processor.process_getOAFriendMids
        self._processMap["searchPaidCallUserRate"] = Processor.process_searchPaidCallUserRate
        self._processMap["getJoinedGroupIdsForChannel"] = Processor.process_getJoinedGroupIdsForChannel
        self._processMap["acquireGroupCallRoute"] = Processor.process_acquireGroupCallRoute
        self._processMap["getUserMidsWhoAddedMe"] = Processor.process_getUserMidsWhoAddedMe
        self._processMap["getIdentityCredential"] = Processor.process_getIdentityCredential
        self._processMap["addOperationForChannel"] = Processor.process_addOperationForChannel
        self._processMap["getSimpleChannelContacts"] = Processor.process_getSimpleChannelContacts
        self._processMap["getUserLastSentMessageTimeStamp"] = Processor.process_getUserLastSentMessageTimeStamp

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_getUserStatus(self, seqid, iprot, oprot):
        args = getUserStatus_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserStatus_result()
        try:
            result.success = self._handler.getUserStatus(args.mid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserStatus", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateProfileAttributeForChannel(self, seqid, iprot, oprot):
        args = updateProfileAttributeForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateProfileAttributeForChannel_result()
        try:
            self._handler.updateProfileAttributeForChannel(args.profileAttribute, args.value)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("updateProfileAttributeForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateExtendedProfileAttribute(self, seqid, iprot, oprot):
        args = updateExtendedProfileAttribute_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateExtendedProfileAttribute_result()
        try:
            self._handler.updateExtendedProfileAttribute(args.attr, args.extendedProfile)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("updateExtendedProfileAttribute", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getAllSimpleChannelContacts(self, seqid, iprot, oprot):
        args = getAllSimpleChannelContacts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAllSimpleChannelContacts_result()
        try:
            result.success = self._handler.getAllSimpleChannelContacts(args.statusSticonFallbackDisabled)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getAllSimpleChannelContacts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUserIdentities(self, seqid, iprot, oprot):
        args = getUserIdentities_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserIdentities_result()
        try:
            result.success = self._handler.getUserIdentities()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserIdentities", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_markPaidCallAd(self, seqid, iprot, oprot):
        args = markPaidCallAd_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = markPaidCallAd_result()
        try:
            result.success = self._handler.markPaidCallAd(args.dialedNumber, args.language, args.disableCallerId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("markPaidCallAd", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_isGroupMember(self, seqid, iprot, oprot):
        args = isGroupMember_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = isGroupMember_result()
        try:
            result.success = self._handler.isGroupMember(args.groupId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("isGroupMember", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPhoneInfoFromPhoneNumber(self, seqid, iprot, oprot):
        args = getPhoneInfoFromPhoneNumber_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPhoneInfoFromPhoneNumber_result()
        try:
            result.success = self._handler.getPhoneInfoFromPhoneNumber(args.region, args.phoneNumber)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPhoneInfoFromPhoneNumber", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_redeemPaidCallVoucher(self, seqid, iprot, oprot):
        args = redeemPaidCallVoucher_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = redeemPaidCallVoucher_result()
        try:
            result.success = self._handler.redeemPaidCallVoucher(args.serial, args.language)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("redeemPaidCallVoucher", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPreferredDisplayName(self, seqid, iprot, oprot):
        args = getPreferredDisplayName_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPreferredDisplayName_result()
        try:
            result.success = self._handler.getPreferredDisplayName(args.mids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPreferredDisplayName", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getContactsForChannel(self, seqid, iprot, oprot):
        args = getContactsForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getContactsForChannel_result()
        try:
            result.success = self._handler.getContactsForChannel(args.ids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getContactsForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCallCreditProducts(self, seqid, iprot, oprot):
        args = getCallCreditProducts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCallCreditProducts_result()
        try:
            result.success = self._handler.getCallCreditProducts(args.appStoreCode, args.pgCode, args.country, args.language)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getCallCreditProducts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCompactContacts(self, seqid, iprot, oprot):
        args = getCompactContacts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCompactContacts_result()
        try:
            result.success = self._handler.getCompactContacts(args.lastModifiedTimestamp)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getCompactContacts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_notifyNotiCenterEvent(self, seqid, iprot, oprot):
        args = notifyNotiCenterEvent_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyNotiCenterEvent_result()
        try:
            self._handler.notifyNotiCenterEvent(args.event)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("notifyNotiCenterEvent", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_isInContact(self, seqid, iprot, oprot):
        args = isInContact_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = isInContact_result()
        try:
            result.success = self._handler.isInContact(args.mid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("isInContact", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_lookupGroupMembers(self, seqid, iprot, oprot):
        args = lookupGroupMembers_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = lookupGroupMembers_result()
        try:
            result.success = self._handler.lookupGroupMembers(args.groupId, args.mids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("lookupGroupMembers", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getRoomInformation(self, seqid, iprot, oprot):
        args = getRoomInformation_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getRoomInformation_result()
        try:
            result.success = self._handler.getRoomInformation(args.roomMid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getRoomInformation", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getGroupCall(self, seqid, iprot, oprot):
        args = getGroupCall_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getGroupCall_result()
        try:
            result.success = self._handler.getGroupCall(args.chatMid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getGroupCall", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_isAllowSecondaryDeviceLogin(self, seqid, iprot, oprot):
        args = isAllowSecondaryDeviceLogin_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = isAllowSecondaryDeviceLogin_result()
        try:
            result.success = self._handler.isAllowSecondaryDeviceLogin()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("isAllowSecondaryDeviceLogin", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPrimaryClientForChannel(self, seqid, iprot, oprot):
        args = getPrimaryClientForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPrimaryClientForChannel_result()
        try:
            result.success = self._handler.getPrimaryClientForChannel()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPrimaryClientForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_createRoomWithBuddy(self, seqid, iprot, oprot):
        args = createRoomWithBuddy_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createRoomWithBuddy_result()
        try:
            result.success = self._handler.createRoomWithBuddy(args.reqSeq, args.buddyMid, args.contactIds)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("createRoomWithBuddy", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getDisplayName(self, seqid, iprot, oprot):
        args = getDisplayName_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDisplayName_result()
        try:
            result.success = self._handler.getDisplayName(args.mid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getDisplayName", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPaidCallMetadata(self, seqid, iprot, oprot):
        args = getPaidCallMetadata_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPaidCallMetadata_result()
        try:
            result.success = self._handler.getPaidCallMetadata(args.language)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPaidCallMetadata", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getMid(self, seqid, iprot, oprot):
        args = getMid_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getMid_result()
        try:
            result.success = self._handler.getMid()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getMid", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUserCountryForBilling(self, seqid, iprot, oprot):
        args = getUserCountryForBilling_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserCountryForBilling_result()
        try:
            result.success = self._handler.getUserCountryForBilling(args.country, args.remoteIp)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserCountryForBilling", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getFavoriteGroupIdsForChannel(self, seqid, iprot, oprot):
        args = getFavoriteGroupIdsForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getFavoriteGroupIdsForChannel_result()
        try:
            result.success = self._handler.getFavoriteGroupIdsForChannel()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getFavoriteGroupIdsForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPaidCallHistory(self, seqid, iprot, oprot):
        args = getPaidCallHistory_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPaidCallHistory_result()
        try:
            result.success = self._handler.getPaidCallHistory(args.start, args.size, args.language)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPaidCallHistory", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendPinCodeOperation(self, seqid, iprot, oprot):
        args = sendPinCodeOperation_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendPinCodeOperation_result()
        try:
            self._handler.sendPinCodeOperation(args.verifier)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("sendPinCodeOperation", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_inviteIntoGroupCall(self, seqid, iprot, oprot):
        args = inviteIntoGroupCall_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = inviteIntoGroupCall_result()
        try:
            self._handler.inviteIntoGroupCall(args.chatMid, args.memberMids, args.mediaType)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("inviteIntoGroupCall", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getFriendMids(self, seqid, iprot, oprot):
        args = getFriendMids_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getFriendMids_result()
        try:
            result.success = self._handler.getFriendMids()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getFriendMids", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getMetaProfile(self, seqid, iprot, oprot):
        args = getMetaProfile_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getMetaProfile_result()
        try:
            result.success = self._handler.getMetaProfile()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getMetaProfile", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendMessageForChannel(self, seqid, iprot, oprot):
        args = sendMessageForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendMessageForChannel_result()
        try:
            result.success = self._handler.sendMessageForChannel(args.message)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("sendMessageForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_activeBuddySubscriberCount(self, seqid, iprot, oprot):
        args = activeBuddySubscriberCount_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = activeBuddySubscriberCount_result()
        try:
            result.success = self._handler.activeBuddySubscriberCount()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("activeBuddySubscriberCount", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCallCreditPurchaseHistory(self, seqid, iprot, oprot):
        args = getCallCreditPurchaseHistory_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCallCreditPurchaseHistory_result()
        try:
            result.success = self._handler.getCallCreditPurchaseHistory(args.request)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getCallCreditPurchaseHistory", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_isRoomMember(self, seqid, iprot, oprot):
        args = isRoomMember_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = isRoomMember_result()
        try:
            result.success = self._handler.isRoomMember(args.roomId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("isRoomMember", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendSystemOAMessage(self, seqid, iprot, oprot):
        args = sendSystemOAMessage_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendSystemOAMessage_result()
        try:
            result.success = self._handler.sendSystemOAMessage(args.message)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("sendSystemOAMessage", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_acquirePaidCallRoute(self, seqid, iprot, oprot):
        args = acquirePaidCallRoute_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = acquirePaidCallRoute_result()
        try:
            result.success = self._handler.acquirePaidCallRoute(args.paidCallType, args.dialedNumber, args.language, args.networkCode, args.disableCallerId, args.referer, args.adSessionId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("acquirePaidCallRoute", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getGroupsForChannel(self, seqid, iprot, oprot):
        args = getGroupsForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getGroupsForChannel_result()
        try:
            result.success = self._handler.getGroupsForChannel(args.groupIds)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getGroupsForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUserCreateTime(self, seqid, iprot, oprot):
        args = getUserCreateTime_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserCreateTime_result()
        try:
            result.success = self._handler.getUserCreateTime()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserCreateTime", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_registerChannelCP(self, seqid, iprot, oprot):
        args = registerChannelCP_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = registerChannelCP_result()
        try:
            result.success = self._handler.registerChannelCP(args.cpId, args.registerPassword)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("registerChannelCP", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_reserveCallCreditPurchase(self, seqid, iprot, oprot):
        args = reserveCallCreditPurchase_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = reserveCallCreditPurchase_result()
        try:
            result.success = self._handler.reserveCallCreditPurchase(args.request)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("reserveCallCreditPurchase", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_acquirePaidCallCurrencyExchangeRate(self, seqid, iprot, oprot):
        args = acquirePaidCallCurrencyExchangeRate_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = acquirePaidCallCurrencyExchangeRate_result()
        try:
            result.success = self._handler.acquirePaidCallCurrencyExchangeRate(args.language)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("acquirePaidCallCurrencyExchangeRate", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getRoomMemberMidsForAppPlatform(self, seqid, iprot, oprot):
        args = getRoomMemberMidsForAppPlatform_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getRoomMemberMidsForAppPlatform_result()
        try:
            result.success = self._handler.getRoomMemberMidsForAppPlatform(args.roomId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getRoomMemberMidsForAppPlatform", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPaidCallBalanceList(self, seqid, iprot, oprot):
        args = getPaidCallBalanceList_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPaidCallBalanceList_result()
        try:
            result.success = self._handler.getPaidCallBalanceList(args.language)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPaidCallBalanceList", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPersonalInfos(self, seqid, iprot, oprot):
        args = getPersonalInfos_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPersonalInfos_result()
        try:
            result.success = self._handler.getPersonalInfos(args.requiredPersonalInfos)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPersonalInfos", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPrimaryClientsForChannel(self, seqid, iprot, oprot):
        args = getPrimaryClientsForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPrimaryClientsForChannel_result()
        try:
            result.success = self._handler.getPrimaryClientsForChannel(args.userMids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPrimaryClientsForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_addBuddyToContact(self, seqid, iprot, oprot):
        args = addBuddyToContact_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addBuddyToContact_result()
        try:
            result.success = self._handler.addBuddyToContact(args.buddyMid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("addBuddyToContact", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getGroupMemberMidsForAppPlatform(self, seqid, iprot, oprot):
        args = getGroupMemberMidsForAppPlatform_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getGroupMemberMidsForAppPlatform_result()
        try:
            result.success = self._handler.getGroupMemberMidsForAppPlatform(args.groupId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getGroupMemberMidsForAppPlatform", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUserLanguage(self, seqid, iprot, oprot):
        args = getUserLanguage_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserLanguage_result()
        try:
            result.success = self._handler.getUserLanguage()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserLanguage", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_lookupPaidCall(self, seqid, iprot, oprot):
        args = lookupPaidCall_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = lookupPaidCall_result()
        try:
            result.success = self._handler.lookupPaidCall(args.dialedNumber, args.language, args.referer)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("lookupPaidCall", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getExtendedProfile(self, seqid, iprot, oprot):
        args = getExtendedProfile_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getExtendedProfile_result()
        try:
            result.success = self._handler.getExtendedProfile()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getExtendedProfile", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getReverseCompactContacts(self, seqid, iprot, oprot):
        args = getReverseCompactContacts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getReverseCompactContacts_result()
        try:
            result.success = self._handler.getReverseCompactContacts(args.ids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getReverseCompactContacts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPaidCallAdStatus(self, seqid, iprot, oprot):
        args = getPaidCallAdStatus_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPaidCallAdStatus_result()
        try:
            result.success = self._handler.getPaidCallAdStatus()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getPaidCallAdStatus", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_findContactByUseridWithoutAbuseBlockForChannel(self, seqid, iprot, oprot):
        args = findContactByUseridWithoutAbuseBlockForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = findContactByUseridWithoutAbuseBlockForChannel_result()
        try:
            result.success = self._handler.findContactByUseridWithoutAbuseBlockForChannel(args.userid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("findContactByUseridWithoutAbuseBlockForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getGroupMemberMids(self, seqid, iprot, oprot):
        args = getGroupMemberMids_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getGroupMemberMids_result()
        try:
            result.success = self._handler.getGroupMemberMids(args.groupId)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getGroupMemberMids", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendMessageWithoutRelationship(self, seqid, iprot, oprot):
        args = sendMessageWithoutRelationship_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendMessageWithoutRelationship_result()
        try:
            result.success = self._handler.sendMessageWithoutRelationship(args.message)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("sendMessageWithoutRelationship", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_displayBuddySubscriberCountInBulk(self, seqid, iprot, oprot):
        args = displayBuddySubscriberCountInBulk_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = displayBuddySubscriberCountInBulk_result()
        try:
            result.success = self._handler.displayBuddySubscriberCountInBulk(args.mids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("displayBuddySubscriberCountInBulk", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_lookupRoomMembers(self, seqid, iprot, oprot):
        args = lookupRoomMembers_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = lookupRoomMembers_result()
        try:
            result.success = self._handler.lookupRoomMembers(args.roomId, args.mids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("lookupRoomMembers", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getFavoriteMidsForChannel(self, seqid, iprot, oprot):
        args = getFavoriteMidsForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getFavoriteMidsForChannel_result()
        try:
            result.success = self._handler.getFavoriteMidsForChannel()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getFavoriteMidsForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getAllContactIdsForChannel(self, seqid, iprot, oprot):
        args = getAllContactIdsForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAllContactIdsForChannel_result()
        try:
            result.success = self._handler.getAllContactIdsForChannel()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getAllContactIdsForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_displayBuddySubscriberCount(self, seqid, iprot, oprot):
        args = displayBuddySubscriberCount_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = displayBuddySubscriberCount_result()
        try:
            result.success = self._handler.displayBuddySubscriberCount()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("displayBuddySubscriberCount", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getProfileForChannel(self, seqid, iprot, oprot):
        args = getProfileForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProfileForChannel_result()
        try:
            result.success = self._handler.getProfileForChannel()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getProfileForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUserTickets(self, seqid, iprot, oprot):
        args = getUserTickets_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserTickets_result()
        try:
            result.success = self._handler.getUserTickets(args.userMids)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserTickets", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getOAFriendMids(self, seqid, iprot, oprot):
        args = getOAFriendMids_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getOAFriendMids_result()
        try:
            result.success = self._handler.getOAFriendMids()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getOAFriendMids", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_searchPaidCallUserRate(self, seqid, iprot, oprot):
        args = searchPaidCallUserRate_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = searchPaidCallUserRate_result()
        try:
            result.success = self._handler.searchPaidCallUserRate(args.countryCode, args.language)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("searchPaidCallUserRate", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getJoinedGroupIdsForChannel(self, seqid, iprot, oprot):
        args = getJoinedGroupIdsForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getJoinedGroupIdsForChannel_result()
        try:
            result.success = self._handler.getJoinedGroupIdsForChannel()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getJoinedGroupIdsForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_acquireGroupCallRoute(self, seqid, iprot, oprot):
        args = acquireGroupCallRoute_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = acquireGroupCallRoute_result()
        try:
            result.success = self._handler.acquireGroupCallRoute(args.chatMid, args.mediaType)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("acquireGroupCallRoute", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUserMidsWhoAddedMe(self, seqid, iprot, oprot):
        args = getUserMidsWhoAddedMe_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserMidsWhoAddedMe_result()
        try:
            result.success = self._handler.getUserMidsWhoAddedMe()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserMidsWhoAddedMe", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getIdentityCredential(self, seqid, iprot, oprot):
        args = getIdentityCredential_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getIdentityCredential_result()
        try:
            result.success = self._handler.getIdentityCredential()
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getIdentityCredential", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_addOperationForChannel(self, seqid, iprot, oprot):
        args = addOperationForChannel_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addOperationForChannel_result()
        try:
            self._handler.addOperationForChannel(args.opType, args.param1, args.param2, args.param3)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("addOperationForChannel", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getSimpleChannelContacts(self, seqid, iprot, oprot):
        args = getSimpleChannelContacts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getSimpleChannelContacts_result()
        try:
            result.success = self._handler.getSimpleChannelContacts(args.ids, args.statusSticonFallbackDisabled)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getSimpleChannelContacts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUserLastSentMessageTimeStamp(self, seqid, iprot, oprot):
        args = getUserLastSentMessageTimeStamp_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUserLastSentMessageTimeStamp_result()
        try:
            result.success = self._handler.getUserLastSentMessageTimeStamp(args.mid)
            msg_type = TMessageType.REPLY
        except TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("getUserLastSentMessageTimeStamp", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class getUserStatus_args(object):
    """
    Attributes:
     - mid
    """


    def __init__(self, mid=None,):
        self.mid = mid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserStatus_args')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserStatus_args)
getUserStatus_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
)


class getUserStatus_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserStatus_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserStatus_result)
getUserStatus_result.thrift_spec = (
    (0, TType.I32, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateProfileAttributeForChannel_args(object):
    """
    Attributes:
     - profileAttribute
     - value
    """


    def __init__(self, profileAttribute=None, value=None,):
        self.profileAttribute = profileAttribute
        self.value = value

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I32:
                    self.profileAttribute = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.value = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateProfileAttributeForChannel_args')
        if self.profileAttribute is not None:
            oprot.writeFieldBegin('profileAttribute', TType.I32, 2)
            oprot.writeI32(self.profileAttribute)
            oprot.writeFieldEnd()
        if self.value is not None:
            oprot.writeFieldBegin('value', TType.STRING, 3)
            oprot.writeString(self.value.encode('utf-8') if sys.version_info[0] == 2 else self.value)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateProfileAttributeForChannel_args)
updateProfileAttributeForChannel_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'profileAttribute', None, None, ),  # 2
    (3, TType.STRING, 'value', 'UTF8', None, ),  # 3
)


class updateProfileAttributeForChannel_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateProfileAttributeForChannel_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateProfileAttributeForChannel_result)
updateProfileAttributeForChannel_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateExtendedProfileAttribute_args(object):
    """
    Attributes:
     - attr
     - extendedProfile
    """


    def __init__(self, attr=None, extendedProfile=None,):
        self.attr = attr
        self.extendedProfile = extendedProfile

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.attr = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.extendedProfile = ExtendedProfile()
                    self.extendedProfile.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateExtendedProfileAttribute_args')
        if self.attr is not None:
            oprot.writeFieldBegin('attr', TType.I32, 1)
            oprot.writeI32(self.attr)
            oprot.writeFieldEnd()
        if self.extendedProfile is not None:
            oprot.writeFieldBegin('extendedProfile', TType.STRUCT, 2)
            self.extendedProfile.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateExtendedProfileAttribute_args)
updateExtendedProfileAttribute_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'attr', None, None, ),  # 1
    (2, TType.STRUCT, 'extendedProfile', [ExtendedProfile, None], None, ),  # 2
)


class updateExtendedProfileAttribute_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('updateExtendedProfileAttribute_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(updateExtendedProfileAttribute_result)
updateExtendedProfileAttribute_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getAllSimpleChannelContacts_args(object):
    """
    Attributes:
     - statusSticonFallbackDisabled
    """


    def __init__(self, statusSticonFallbackDisabled=None,):
        self.statusSticonFallbackDisabled = statusSticonFallbackDisabled

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BOOL:
                    self.statusSticonFallbackDisabled = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getAllSimpleChannelContacts_args')
        if self.statusSticonFallbackDisabled is not None:
            oprot.writeFieldBegin('statusSticonFallbackDisabled', TType.BOOL, 1)
            oprot.writeBool(self.statusSticonFallbackDisabled)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getAllSimpleChannelContacts_args)
getAllSimpleChannelContacts_args.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'statusSticonFallbackDisabled', None, None, ),  # 1
)


class getAllSimpleChannelContacts_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2101, _size2098) = iprot.readListBegin()
                    for _i2102 in range(_size2098):
                        _elem2103 = SimpleChannelContact()
                        _elem2103.read(iprot)
                        self.success.append(_elem2103)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getAllSimpleChannelContacts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2104 in self.success:
                iter2104.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getAllSimpleChannelContacts_result)
getAllSimpleChannelContacts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [SimpleChannelContact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUserIdentities_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserIdentities_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserIdentities_args)
getUserIdentities_args.thrift_spec = (
)


class getUserIdentities_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.MAP:
                    self.success = {}
                    (_ktype2106, _vtype2107, _size2105) = iprot.readMapBegin()
                    for _i2109 in range(_size2105):
                        _key2110 = iprot.readI32()
                        _val2111 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success[_key2110] = _val2111
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserIdentities_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.success))
            for kiter2112, viter2113 in self.success.items():
                oprot.writeI32(kiter2112)
                oprot.writeString(viter2113.encode('utf-8') if sys.version_info[0] == 2 else viter2113)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserIdentities_result)
getUserIdentities_result.thrift_spec = (
    (0, TType.MAP, 'success', (TType.I32, None, TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class markPaidCallAd_args(object):
    """
    Attributes:
     - dialedNumber
     - language
     - disableCallerId
    """


    def __init__(self, dialedNumber=None, language=None, disableCallerId=None,):
        self.dialedNumber = dialedNumber
        self.language = language
        self.disableCallerId = disableCallerId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.dialedNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.disableCallerId = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('markPaidCallAd_args')
        if self.dialedNumber is not None:
            oprot.writeFieldBegin('dialedNumber', TType.STRING, 2)
            oprot.writeString(self.dialedNumber.encode('utf-8') if sys.version_info[0] == 2 else self.dialedNumber)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.disableCallerId is not None:
            oprot.writeFieldBegin('disableCallerId', TType.BOOL, 4)
            oprot.writeBool(self.disableCallerId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(markPaidCallAd_args)
markPaidCallAd_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'dialedNumber', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
    (4, TType.BOOL, 'disableCallerId', None, None, ),  # 4
)


class markPaidCallAd_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaidCallDialing()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('markPaidCallAd_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(markPaidCallAd_result)
markPaidCallAd_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaidCallDialing, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class isGroupMember_args(object):
    """
    Attributes:
     - groupId
    """


    def __init__(self, groupId=None,):
        self.groupId = groupId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.groupId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isGroupMember_args')
        if self.groupId is not None:
            oprot.writeFieldBegin('groupId', TType.STRING, 1)
            oprot.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isGroupMember_args)
isGroupMember_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'groupId', 'UTF8', None, ),  # 1
)


class isGroupMember_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isGroupMember_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isGroupMember_result)
isGroupMember_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPhoneInfoFromPhoneNumber_args(object):
    """
    Attributes:
     - region
     - phoneNumber
    """


    def __init__(self, region=None, phoneNumber=None,):
        self.region = region
        self.phoneNumber = phoneNumber

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.region = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.phoneNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPhoneInfoFromPhoneNumber_args')
        if self.region is not None:
            oprot.writeFieldBegin('region', TType.STRING, 1)
            oprot.writeString(self.region.encode('utf-8') if sys.version_info[0] == 2 else self.region)
            oprot.writeFieldEnd()
        if self.phoneNumber is not None:
            oprot.writeFieldBegin('phoneNumber', TType.STRING, 2)
            oprot.writeString(self.phoneNumber.encode('utf-8') if sys.version_info[0] == 2 else self.phoneNumber)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPhoneInfoFromPhoneNumber_args)
getPhoneInfoFromPhoneNumber_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'region', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'phoneNumber', 'UTF8', None, ),  # 2
)


class getPhoneInfoFromPhoneNumber_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PhoneInfoForChannel()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPhoneInfoFromPhoneNumber_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPhoneInfoFromPhoneNumber_result)
getPhoneInfoFromPhoneNumber_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PhoneInfoForChannel, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class redeemPaidCallVoucher_args(object):
    """
    Attributes:
     - serial
     - language
    """


    def __init__(self, serial=None, language=None,):
        self.serial = serial
        self.language = language

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.serial = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('redeemPaidCallVoucher_args')
        if self.serial is not None:
            oprot.writeFieldBegin('serial', TType.STRING, 2)
            oprot.writeString(self.serial.encode('utf-8') if sys.version_info[0] == 2 else self.serial)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(redeemPaidCallVoucher_args)
redeemPaidCallVoucher_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'serial', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
)


class redeemPaidCallVoucher_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaidCallRedeemResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('redeemPaidCallVoucher_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(redeemPaidCallVoucher_result)
redeemPaidCallVoucher_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaidCallRedeemResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPreferredDisplayName_args(object):
    """
    Attributes:
     - mids
    """


    def __init__(self, mids=None,):
        self.mids = mids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype2117, _size2114) = iprot.readListBegin()
                    for _i2118 in range(_size2114):
                        _elem2119 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem2119)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPreferredDisplayName_args')
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter2120 in self.mids:
                oprot.writeString(iter2120.encode('utf-8') if sys.version_info[0] == 2 else iter2120)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPreferredDisplayName_args)
getPreferredDisplayName_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class getPreferredDisplayName_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.MAP:
                    self.success = {}
                    (_ktype2122, _vtype2123, _size2121) = iprot.readMapBegin()
                    for _i2125 in range(_size2121):
                        _key2126 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val2127 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success[_key2126] = _val2127
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPreferredDisplayName_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.success))
            for kiter2128, viter2129 in self.success.items():
                oprot.writeString(kiter2128.encode('utf-8') if sys.version_info[0] == 2 else kiter2128)
                oprot.writeString(viter2129.encode('utf-8') if sys.version_info[0] == 2 else viter2129)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPreferredDisplayName_result)
getPreferredDisplayName_result.thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getContactsForChannel_args(object):
    """
    Attributes:
     - ids
    """


    def __init__(self, ids=None,):
        self.ids = ids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.LIST:
                    self.ids = []
                    (_etype2133, _size2130) = iprot.readListBegin()
                    for _i2134 in range(_size2130):
                        _elem2135 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.ids.append(_elem2135)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getContactsForChannel_args')
        if self.ids is not None:
            oprot.writeFieldBegin('ids', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.ids))
            for iter2136 in self.ids:
                oprot.writeString(iter2136.encode('utf-8') if sys.version_info[0] == 2 else iter2136)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getContactsForChannel_args)
getContactsForChannel_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.LIST, 'ids', (TType.STRING, 'UTF8', False), None, ),  # 2
)


class getContactsForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2140, _size2137) = iprot.readListBegin()
                    for _i2141 in range(_size2137):
                        _elem2142 = Contact()
                        _elem2142.read(iprot)
                        self.success.append(_elem2142)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getContactsForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2143 in self.success:
                iter2143.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getContactsForChannel_result)
getContactsForChannel_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [Contact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCallCreditProducts_args(object):
    """
    Attributes:
     - appStoreCode
     - pgCode
     - country
     - language
    """


    def __init__(self, appStoreCode=None, pgCode=None, country=None, language=None,):
        self.appStoreCode = appStoreCode
        self.pgCode = pgCode
        self.country = country
        self.language = language

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I32:
                    self.appStoreCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.pgCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCallCreditProducts_args')
        if self.appStoreCode is not None:
            oprot.writeFieldBegin('appStoreCode', TType.I32, 2)
            oprot.writeI32(self.appStoreCode)
            oprot.writeFieldEnd()
        if self.pgCode is not None:
            oprot.writeFieldBegin('pgCode', TType.I32, 3)
            oprot.writeI32(self.pgCode)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 4)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 5)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCallCreditProducts_args)
getCallCreditProducts_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'appStoreCode', None, None, ),  # 2
    (3, TType.I32, 'pgCode', None, None, ),  # 3
    (4, TType.STRING, 'country', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'language', 'UTF8', None, ),  # 5
)


class getCallCreditProducts_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2147, _size2144) = iprot.readListBegin()
                    for _i2148 in range(_size2144):
                        _elem2149 = CoinProductItem()
                        _elem2149.read(iprot)
                        self.success.append(_elem2149)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCallCreditProducts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2150 in self.success:
                iter2150.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCallCreditProducts_result)
getCallCreditProducts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [CoinProductItem, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCompactContacts_args(object):
    """
    Attributes:
     - lastModifiedTimestamp
    """


    def __init__(self, lastModifiedTimestamp=None,):
        self.lastModifiedTimestamp = lastModifiedTimestamp

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.lastModifiedTimestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCompactContacts_args')
        if self.lastModifiedTimestamp is not None:
            oprot.writeFieldBegin('lastModifiedTimestamp', TType.I64, 2)
            oprot.writeI64(self.lastModifiedTimestamp)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCompactContacts_args)
getCompactContacts_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'lastModifiedTimestamp', None, None, ),  # 2
)


class getCompactContacts_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2154, _size2151) = iprot.readListBegin()
                    for _i2155 in range(_size2151):
                        _elem2156 = CompactContact()
                        _elem2156.read(iprot)
                        self.success.append(_elem2156)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCompactContacts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2157 in self.success:
                iter2157.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCompactContacts_result)
getCompactContacts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [CompactContact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class notifyNotiCenterEvent_args(object):
    """
    Attributes:
     - event
    """


    def __init__(self, event=None,):
        self.event = event

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.event = NotiCenterEventData()
                    self.event.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('notifyNotiCenterEvent_args')
        if self.event is not None:
            oprot.writeFieldBegin('event', TType.STRUCT, 1)
            self.event.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(notifyNotiCenterEvent_args)
notifyNotiCenterEvent_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'event', [NotiCenterEventData, None], None, ),  # 1
)


class notifyNotiCenterEvent_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('notifyNotiCenterEvent_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(notifyNotiCenterEvent_result)
notifyNotiCenterEvent_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class isInContact_args(object):
    """
    Attributes:
     - mid
    """


    def __init__(self, mid=None,):
        self.mid = mid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isInContact_args')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 2)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isInContact_args)
isInContact_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'mid', 'UTF8', None, ),  # 2
)


class isInContact_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isInContact_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isInContact_result)
isInContact_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class lookupGroupMembers_args(object):
    """
    Attributes:
     - groupId
     - mids
    """


    def __init__(self, groupId=None, mids=None,):
        self.groupId = groupId
        self.mids = mids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.groupId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype2161, _size2158) = iprot.readListBegin()
                    for _i2162 in range(_size2158):
                        _elem2163 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem2163)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupGroupMembers_args')
        if self.groupId is not None:
            oprot.writeFieldBegin('groupId', TType.STRING, 1)
            oprot.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter2164 in self.mids:
                oprot.writeString(iter2164.encode('utf-8') if sys.version_info[0] == 2 else iter2164)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupGroupMembers_args)
lookupGroupMembers_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'groupId', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 2
)


class lookupGroupMembers_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2168, _size2165) = iprot.readListBegin()
                    for _i2169 in range(_size2165):
                        _elem2170 = SimpleChannelContact()
                        _elem2170.read(iprot)
                        self.success.append(_elem2170)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupGroupMembers_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2171 in self.success:
                iter2171.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupGroupMembers_result)
lookupGroupMembers_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [SimpleChannelContact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getRoomInformation_args(object):
    """
    Attributes:
     - roomMid
    """


    def __init__(self, roomMid=None,):
        self.roomMid = roomMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.roomMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getRoomInformation_args')
        if self.roomMid is not None:
            oprot.writeFieldBegin('roomMid', TType.STRING, 1)
            oprot.writeString(self.roomMid.encode('utf-8') if sys.version_info[0] == 2 else self.roomMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getRoomInformation_args)
getRoomInformation_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'roomMid', 'UTF8', None, ),  # 1
)


class getRoomInformation_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Room()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getRoomInformation_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getRoomInformation_result)
getRoomInformation_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Room, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getGroupCall_args(object):
    """
    Attributes:
     - chatMid
    """


    def __init__(self, chatMid=None,):
        self.chatMid = chatMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.chatMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupCall_args')
        if self.chatMid is not None:
            oprot.writeFieldBegin('chatMid', TType.STRING, 2)
            oprot.writeString(self.chatMid.encode('utf-8') if sys.version_info[0] == 2 else self.chatMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupCall_args)
getGroupCall_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'chatMid', 'UTF8', None, ),  # 2
)


class getGroupCall_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = GroupCall()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupCall_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupCall_result)
getGroupCall_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [GroupCall, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class isAllowSecondaryDeviceLogin_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isAllowSecondaryDeviceLogin_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isAllowSecondaryDeviceLogin_args)
isAllowSecondaryDeviceLogin_args.thrift_spec = (
)


class isAllowSecondaryDeviceLogin_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isAllowSecondaryDeviceLogin_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isAllowSecondaryDeviceLogin_result)
isAllowSecondaryDeviceLogin_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPrimaryClientForChannel_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPrimaryClientForChannel_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPrimaryClientForChannel_args)
getPrimaryClientForChannel_args.thrift_spec = (
)


class getPrimaryClientForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = SimpleChannelClient()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPrimaryClientForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPrimaryClientForChannel_result)
getPrimaryClientForChannel_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SimpleChannelClient, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class createRoomWithBuddy_args(object):
    """
    Attributes:
     - reqSeq
     - buddyMid
     - contactIds
    """


    def __init__(self, reqSeq=None, buddyMid=None, contactIds=None,):
        self.reqSeq = reqSeq
        self.buddyMid = buddyMid
        self.contactIds = contactIds

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.reqSeq = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.buddyMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.contactIds = []
                    (_etype2175, _size2172) = iprot.readListBegin()
                    for _i2176 in range(_size2172):
                        _elem2177 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.contactIds.append(_elem2177)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('createRoomWithBuddy_args')
        if self.reqSeq is not None:
            oprot.writeFieldBegin('reqSeq', TType.I32, 1)
            oprot.writeI32(self.reqSeq)
            oprot.writeFieldEnd()
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
            oprot.writeString(self.buddyMid.encode('utf-8') if sys.version_info[0] == 2 else self.buddyMid)
            oprot.writeFieldEnd()
        if self.contactIds is not None:
            oprot.writeFieldBegin('contactIds', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.contactIds))
            for iter2178 in self.contactIds:
                oprot.writeString(iter2178.encode('utf-8') if sys.version_info[0] == 2 else iter2178)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(createRoomWithBuddy_args)
createRoomWithBuddy_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'reqSeq', None, None, ),  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
    (3, TType.LIST, 'contactIds', (TType.STRING, 'UTF8', False), None, ),  # 3
)


class createRoomWithBuddy_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Room()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('createRoomWithBuddy_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(createRoomWithBuddy_result)
createRoomWithBuddy_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Room, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getDisplayName_args(object):
    """
    Attributes:
     - mid
    """


    def __init__(self, mid=None,):
        self.mid = mid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getDisplayName_args')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 2)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getDisplayName_args)
getDisplayName_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'mid', 'UTF8', None, ),  # 2
)


class getDisplayName_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getDisplayName_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getDisplayName_result)
getDisplayName_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPaidCallMetadata_args(object):
    """
    Attributes:
     - language
    """


    def __init__(self, language=None,):
        self.language = language

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallMetadata_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallMetadata_args)
getPaidCallMetadata_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
)


class getPaidCallMetadata_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaidCallMetadataResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallMetadata_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallMetadata_result)
getPaidCallMetadata_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaidCallMetadataResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getMid_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getMid_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getMid_args)
getMid_args.thrift_spec = (
)


class getMid_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getMid_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getMid_result)
getMid_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUserCountryForBilling_args(object):
    """
    Attributes:
     - country
     - remoteIp
    """


    def __init__(self, country=None, remoteIp=None,):
        self.country = country
        self.remoteIp = remoteIp

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.remoteIp = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserCountryForBilling_args')
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 2)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.remoteIp is not None:
            oprot.writeFieldBegin('remoteIp', TType.STRING, 3)
            oprot.writeString(self.remoteIp.encode('utf-8') if sys.version_info[0] == 2 else self.remoteIp)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserCountryForBilling_args)
getUserCountryForBilling_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'country', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'remoteIp', 'UTF8', None, ),  # 3
)


class getUserCountryForBilling_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserCountryForBilling_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserCountryForBilling_result)
getUserCountryForBilling_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getFavoriteGroupIdsForChannel_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFavoriteGroupIdsForChannel_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFavoriteGroupIdsForChannel_args)
getFavoriteGroupIdsForChannel_args.thrift_spec = (
)


class getFavoriteGroupIdsForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2182, _size2179) = iprot.readListBegin()
                    for _i2183 in range(_size2179):
                        _elem2184 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2184)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFavoriteGroupIdsForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2185 in self.success:
                oprot.writeString(iter2185.encode('utf-8') if sys.version_info[0] == 2 else iter2185)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFavoriteGroupIdsForChannel_result)
getFavoriteGroupIdsForChannel_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPaidCallHistory_args(object):
    """
    Attributes:
     - start
     - size
     - language
    """


    def __init__(self, start=None, size=None, language=None,):
        self.start = start
        self.size = size
        self.language = language

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I64:
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallHistory_args')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 2)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 3)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallHistory_args)
getPaidCallHistory_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I64, 'start', None, None, ),  # 2
    (3, TType.I32, 'size', None, None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
)


class getPaidCallHistory_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaidCallHistoryResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallHistory_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallHistory_result)
getPaidCallHistory_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaidCallHistoryResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendPinCodeOperation_args(object):
    """
    Attributes:
     - verifier
    """


    def __init__(self, verifier=None,):
        self.verifier = verifier

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendPinCodeOperation_args')
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 1)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendPinCodeOperation_args)
sendPinCodeOperation_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'verifier', 'UTF8', None, ),  # 1
)


class sendPinCodeOperation_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendPinCodeOperation_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendPinCodeOperation_result)
sendPinCodeOperation_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class inviteIntoGroupCall_args(object):
    """
    Attributes:
     - chatMid
     - memberMids
     - mediaType
    """


    def __init__(self, chatMid=None, memberMids=None, mediaType=None,):
        self.chatMid = chatMid
        self.memberMids = memberMids
        self.mediaType = mediaType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.chatMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.memberMids = []
                    (_etype2189, _size2186) = iprot.readListBegin()
                    for _i2190 in range(_size2186):
                        _elem2191 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.memberMids.append(_elem2191)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.mediaType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('inviteIntoGroupCall_args')
        if self.chatMid is not None:
            oprot.writeFieldBegin('chatMid', TType.STRING, 2)
            oprot.writeString(self.chatMid.encode('utf-8') if sys.version_info[0] == 2 else self.chatMid)
            oprot.writeFieldEnd()
        if self.memberMids is not None:
            oprot.writeFieldBegin('memberMids', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.memberMids))
            for iter2192 in self.memberMids:
                oprot.writeString(iter2192.encode('utf-8') if sys.version_info[0] == 2 else iter2192)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.mediaType is not None:
            oprot.writeFieldBegin('mediaType', TType.I32, 4)
            oprot.writeI32(self.mediaType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(inviteIntoGroupCall_args)
inviteIntoGroupCall_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'chatMid', 'UTF8', None, ),  # 2
    (3, TType.LIST, 'memberMids', (TType.STRING, 'UTF8', False), None, ),  # 3
    (4, TType.I32, 'mediaType', None, None, ),  # 4
)


class inviteIntoGroupCall_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('inviteIntoGroupCall_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(inviteIntoGroupCall_result)
inviteIntoGroupCall_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getFriendMids_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFriendMids_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFriendMids_args)
getFriendMids_args.thrift_spec = (
)


class getFriendMids_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2196, _size2193) = iprot.readListBegin()
                    for _i2197 in range(_size2193):
                        _elem2198 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2198)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFriendMids_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2199 in self.success:
                oprot.writeString(iter2199.encode('utf-8') if sys.version_info[0] == 2 else iter2199)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFriendMids_result)
getFriendMids_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getMetaProfile_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getMetaProfile_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getMetaProfile_args)
getMetaProfile_args.thrift_spec = (
)


class getMetaProfile_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = MetaProfile()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getMetaProfile_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getMetaProfile_result)
getMetaProfile_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [MetaProfile, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendMessageForChannel_args(object):
    """
    Attributes:
     - message
    """


    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.message = Message()
                    self.message.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendMessageForChannel_args')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRUCT, 2)
            self.message.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendMessageForChannel_args)
sendMessageForChannel_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'message', [Message, None], None, ),  # 2
)


class sendMessageForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Message()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendMessageForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendMessageForChannel_result)
sendMessageForChannel_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Message, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class activeBuddySubscriberCount_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('activeBuddySubscriberCount_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(activeBuddySubscriberCount_args)
activeBuddySubscriberCount_args.thrift_spec = (
)


class activeBuddySubscriberCount_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('activeBuddySubscriberCount_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(activeBuddySubscriberCount_result)
activeBuddySubscriberCount_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCallCreditPurchaseHistory_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.request = CoinHistoryCondition()
                    self.request.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCallCreditPurchaseHistory_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 2)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCallCreditPurchaseHistory_args)
getCallCreditPurchaseHistory_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'request', [CoinHistoryCondition, None], None, ),  # 2
)


class getCallCreditPurchaseHistory_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = CoinHistoryResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getCallCreditPurchaseHistory_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getCallCreditPurchaseHistory_result)
getCallCreditPurchaseHistory_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [CoinHistoryResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class isRoomMember_args(object):
    """
    Attributes:
     - roomId
    """


    def __init__(self, roomId=None,):
        self.roomId = roomId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.roomId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isRoomMember_args')
        if self.roomId is not None:
            oprot.writeFieldBegin('roomId', TType.STRING, 1)
            oprot.writeString(self.roomId.encode('utf-8') if sys.version_info[0] == 2 else self.roomId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isRoomMember_args)
isRoomMember_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'roomId', 'UTF8', None, ),  # 1
)


class isRoomMember_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('isRoomMember_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(isRoomMember_result)
isRoomMember_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendSystemOAMessage_args(object):
    """
    Attributes:
     - message
    """


    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.message = Message()
                    self.message.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendSystemOAMessage_args')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRUCT, 1)
            self.message.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendSystemOAMessage_args)
sendSystemOAMessage_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'message', [Message, None], None, ),  # 1
)


class sendSystemOAMessage_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Message()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendSystemOAMessage_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendSystemOAMessage_result)
sendSystemOAMessage_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Message, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class acquirePaidCallRoute_args(object):
    """
    Attributes:
     - paidCallType
     - dialedNumber
     - language
     - networkCode
     - disableCallerId
     - referer
     - adSessionId
    """


    def __init__(self, paidCallType=None, dialedNumber=None, language=None, networkCode=None, disableCallerId=None, referer=None, adSessionId=None,):
        self.paidCallType = paidCallType
        self.dialedNumber = dialedNumber
        self.language = language
        self.networkCode = networkCode
        self.disableCallerId = disableCallerId
        self.referer = referer
        self.adSessionId = adSessionId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.I32:
                    self.paidCallType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.dialedNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.networkCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BOOL:
                    self.disableCallerId = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.referer = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.adSessionId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('acquirePaidCallRoute_args')
        if self.paidCallType is not None:
            oprot.writeFieldBegin('paidCallType', TType.I32, 2)
            oprot.writeI32(self.paidCallType)
            oprot.writeFieldEnd()
        if self.dialedNumber is not None:
            oprot.writeFieldBegin('dialedNumber', TType.STRING, 3)
            oprot.writeString(self.dialedNumber.encode('utf-8') if sys.version_info[0] == 2 else self.dialedNumber)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 4)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.networkCode is not None:
            oprot.writeFieldBegin('networkCode', TType.STRING, 5)
            oprot.writeString(self.networkCode.encode('utf-8') if sys.version_info[0] == 2 else self.networkCode)
            oprot.writeFieldEnd()
        if self.disableCallerId is not None:
            oprot.writeFieldBegin('disableCallerId', TType.BOOL, 6)
            oprot.writeBool(self.disableCallerId)
            oprot.writeFieldEnd()
        if self.referer is not None:
            oprot.writeFieldBegin('referer', TType.STRING, 7)
            oprot.writeString(self.referer.encode('utf-8') if sys.version_info[0] == 2 else self.referer)
            oprot.writeFieldEnd()
        if self.adSessionId is not None:
            oprot.writeFieldBegin('adSessionId', TType.STRING, 8)
            oprot.writeString(self.adSessionId.encode('utf-8') if sys.version_info[0] == 2 else self.adSessionId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(acquirePaidCallRoute_args)
acquirePaidCallRoute_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'paidCallType', None, None, ),  # 2
    (3, TType.STRING, 'dialedNumber', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'language', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'networkCode', 'UTF8', None, ),  # 5
    (6, TType.BOOL, 'disableCallerId', None, None, ),  # 6
    (7, TType.STRING, 'referer', 'UTF8', None, ),  # 7
    (8, TType.STRING, 'adSessionId', 'UTF8', None, ),  # 8
)


class acquirePaidCallRoute_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaidCallResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('acquirePaidCallRoute_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(acquirePaidCallRoute_result)
acquirePaidCallRoute_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaidCallResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getGroupsForChannel_args(object):
    """
    Attributes:
     - groupIds
    """


    def __init__(self, groupIds=None,):
        self.groupIds = groupIds

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.groupIds = []
                    (_etype2203, _size2200) = iprot.readListBegin()
                    for _i2204 in range(_size2200):
                        _elem2205 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.groupIds.append(_elem2205)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupsForChannel_args')
        if self.groupIds is not None:
            oprot.writeFieldBegin('groupIds', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.groupIds))
            for iter2206 in self.groupIds:
                oprot.writeString(iter2206.encode('utf-8') if sys.version_info[0] == 2 else iter2206)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupsForChannel_args)
getGroupsForChannel_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'groupIds', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class getGroupsForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2210, _size2207) = iprot.readListBegin()
                    for _i2211 in range(_size2207):
                        _elem2212 = Group()
                        _elem2212.read(iprot)
                        self.success.append(_elem2212)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupsForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2213 in self.success:
                iter2213.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupsForChannel_result)
getGroupsForChannel_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [Group, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUserCreateTime_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserCreateTime_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserCreateTime_args)
getUserCreateTime_args.thrift_spec = (
)


class getUserCreateTime_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserCreateTime_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserCreateTime_result)
getUserCreateTime_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class registerChannelCP_args(object):
    """
    Attributes:
     - cpId
     - registerPassword
    """


    def __init__(self, cpId=None, registerPassword=None,):
        self.cpId = cpId
        self.registerPassword = registerPassword

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.cpId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.registerPassword = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('registerChannelCP_args')
        if self.cpId is not None:
            oprot.writeFieldBegin('cpId', TType.STRING, 2)
            oprot.writeString(self.cpId.encode('utf-8') if sys.version_info[0] == 2 else self.cpId)
            oprot.writeFieldEnd()
        if self.registerPassword is not None:
            oprot.writeFieldBegin('registerPassword', TType.STRING, 3)
            oprot.writeString(self.registerPassword.encode('utf-8') if sys.version_info[0] == 2 else self.registerPassword)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(registerChannelCP_args)
registerChannelCP_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'cpId', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'registerPassword', 'UTF8', None, ),  # 3
)


class registerChannelCP_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('registerChannelCP_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(registerChannelCP_result)
registerChannelCP_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class reserveCallCreditPurchase_args(object):
    """
    Attributes:
     - request
    """


    def __init__(self, request=None,):
        self.request = request

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.request = CoinPurchaseReservation()
                    self.request.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('reserveCallCreditPurchase_args')
        if self.request is not None:
            oprot.writeFieldBegin('request', TType.STRUCT, 2)
            self.request.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(reserveCallCreditPurchase_args)
reserveCallCreditPurchase_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'request', [CoinPurchaseReservation, None], None, ),  # 2
)


class reserveCallCreditPurchase_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaymentReservationResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('reserveCallCreditPurchase_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(reserveCallCreditPurchase_result)
reserveCallCreditPurchase_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaymentReservationResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class acquirePaidCallCurrencyExchangeRate_args(object):
    """
    Attributes:
     - language
    """


    def __init__(self, language=None,):
        self.language = language

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('acquirePaidCallCurrencyExchangeRate_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(acquirePaidCallCurrencyExchangeRate_args)
acquirePaidCallCurrencyExchangeRate_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
)


class acquirePaidCallCurrencyExchangeRate_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2217, _size2214) = iprot.readListBegin()
                    for _i2218 in range(_size2214):
                        _elem2219 = PaidCallCurrencyExchangeRate()
                        _elem2219.read(iprot)
                        self.success.append(_elem2219)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('acquirePaidCallCurrencyExchangeRate_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2220 in self.success:
                iter2220.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(acquirePaidCallCurrencyExchangeRate_result)
acquirePaidCallCurrencyExchangeRate_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [PaidCallCurrencyExchangeRate, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getRoomMemberMidsForAppPlatform_args(object):
    """
    Attributes:
     - roomId
    """


    def __init__(self, roomId=None,):
        self.roomId = roomId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.roomId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getRoomMemberMidsForAppPlatform_args')
        if self.roomId is not None:
            oprot.writeFieldBegin('roomId', TType.STRING, 1)
            oprot.writeString(self.roomId.encode('utf-8') if sys.version_info[0] == 2 else self.roomId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getRoomMemberMidsForAppPlatform_args)
getRoomMemberMidsForAppPlatform_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'roomId', 'UTF8', None, ),  # 1
)


class getRoomMemberMidsForAppPlatform_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2224, _size2221) = iprot.readListBegin()
                    for _i2225 in range(_size2221):
                        _elem2226 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2226)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getRoomMemberMidsForAppPlatform_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2227 in self.success:
                oprot.writeString(iter2227.encode('utf-8') if sys.version_info[0] == 2 else iter2227)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getRoomMemberMidsForAppPlatform_result)
getRoomMemberMidsForAppPlatform_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPaidCallBalanceList_args(object):
    """
    Attributes:
     - language
    """


    def __init__(self, language=None,):
        self.language = language

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallBalanceList_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallBalanceList_args)
getPaidCallBalanceList_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
)


class getPaidCallBalanceList_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2231, _size2228) = iprot.readListBegin()
                    for _i2232 in range(_size2228):
                        _elem2233 = PaidCallBalance()
                        _elem2233.read(iprot)
                        self.success.append(_elem2233)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallBalanceList_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2234 in self.success:
                iter2234.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallBalanceList_result)
getPaidCallBalanceList_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [PaidCallBalance, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPersonalInfos_args(object):
    """
    Attributes:
     - requiredPersonalInfos
    """


    def __init__(self, requiredPersonalInfos=None,):
        self.requiredPersonalInfos = requiredPersonalInfos

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.SET:
                    self.requiredPersonalInfos = set()
                    (_etype2238, _size2235) = iprot.readSetBegin()
                    for _i2239 in range(_size2235):
                        _elem2240 = iprot.readI32()
                        self.requiredPersonalInfos.add(_elem2240)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPersonalInfos_args')
        if self.requiredPersonalInfos is not None:
            oprot.writeFieldBegin('requiredPersonalInfos', TType.SET, 1)
            oprot.writeSetBegin(TType.I32, len(self.requiredPersonalInfos))
            for iter2241 in self.requiredPersonalInfos:
                oprot.writeI32(iter2241)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPersonalInfos_args)
getPersonalInfos_args.thrift_spec = (
    None,  # 0
    (1, TType.SET, 'requiredPersonalInfos', (TType.I32, None, False), None, ),  # 1
)


class getPersonalInfos_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.MAP:
                    self.success = {}
                    (_ktype2243, _vtype2244, _size2242) = iprot.readMapBegin()
                    for _i2246 in range(_size2242):
                        _key2247 = iprot.readI32()
                        _val2248 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success[_key2247] = _val2248
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPersonalInfos_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.success))
            for kiter2249, viter2250 in self.success.items():
                oprot.writeI32(kiter2249)
                oprot.writeString(viter2250.encode('utf-8') if sys.version_info[0] == 2 else viter2250)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPersonalInfos_result)
getPersonalInfos_result.thrift_spec = (
    (0, TType.MAP, 'success', (TType.I32, None, TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPrimaryClientsForChannel_args(object):
    """
    Attributes:
     - userMids
    """


    def __init__(self, userMids=None,):
        self.userMids = userMids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.userMids = []
                    (_etype2254, _size2251) = iprot.readListBegin()
                    for _i2255 in range(_size2251):
                        _elem2256 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.userMids.append(_elem2256)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPrimaryClientsForChannel_args')
        if self.userMids is not None:
            oprot.writeFieldBegin('userMids', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.userMids))
            for iter2257 in self.userMids:
                oprot.writeString(iter2257.encode('utf-8') if sys.version_info[0] == 2 else iter2257)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPrimaryClientsForChannel_args)
getPrimaryClientsForChannel_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'userMids', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class getPrimaryClientsForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2261, _size2258) = iprot.readListBegin()
                    for _i2262 in range(_size2258):
                        _elem2263 = SimpleChannelClient()
                        _elem2263.read(iprot)
                        self.success.append(_elem2263)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPrimaryClientsForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2264 in self.success:
                iter2264.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPrimaryClientsForChannel_result)
getPrimaryClientsForChannel_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [SimpleChannelClient, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class addBuddyToContact_args(object):
    """
    Attributes:
     - buddyMid
    """


    def __init__(self, buddyMid=None,):
        self.buddyMid = buddyMid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.buddyMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('addBuddyToContact_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 1)
            oprot.writeString(self.buddyMid.encode('utf-8') if sys.version_info[0] == 2 else self.buddyMid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(addBuddyToContact_args)
addBuddyToContact_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 1
)


class addBuddyToContact_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ContactTransition()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('addBuddyToContact_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(addBuddyToContact_result)
addBuddyToContact_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ContactTransition, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getGroupMemberMidsForAppPlatform_args(object):
    """
    Attributes:
     - groupId
    """


    def __init__(self, groupId=None,):
        self.groupId = groupId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.groupId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupMemberMidsForAppPlatform_args')
        if self.groupId is not None:
            oprot.writeFieldBegin('groupId', TType.STRING, 1)
            oprot.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupMemberMidsForAppPlatform_args)
getGroupMemberMidsForAppPlatform_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'groupId', 'UTF8', None, ),  # 1
)


class getGroupMemberMidsForAppPlatform_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2268, _size2265) = iprot.readListBegin()
                    for _i2269 in range(_size2265):
                        _elem2270 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2270)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupMemberMidsForAppPlatform_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2271 in self.success:
                oprot.writeString(iter2271.encode('utf-8') if sys.version_info[0] == 2 else iter2271)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupMemberMidsForAppPlatform_result)
getGroupMemberMidsForAppPlatform_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUserLanguage_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserLanguage_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserLanguage_args)
getUserLanguage_args.thrift_spec = (
)


class getUserLanguage_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserLanguage_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserLanguage_result)
getUserLanguage_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class lookupPaidCall_args(object):
    """
    Attributes:
     - dialedNumber
     - language
     - referer
    """


    def __init__(self, dialedNumber=None, language=None, referer=None,):
        self.dialedNumber = dialedNumber
        self.language = language
        self.referer = referer

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.dialedNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.referer = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupPaidCall_args')
        if self.dialedNumber is not None:
            oprot.writeFieldBegin('dialedNumber', TType.STRING, 2)
            oprot.writeString(self.dialedNumber.encode('utf-8') if sys.version_info[0] == 2 else self.dialedNumber)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.referer is not None:
            oprot.writeFieldBegin('referer', TType.STRING, 4)
            oprot.writeString(self.referer.encode('utf-8') if sys.version_info[0] == 2 else self.referer)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupPaidCall_args)
lookupPaidCall_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'dialedNumber', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'referer', 'UTF8', None, ),  # 4
)


class lookupPaidCall_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaidCallResponse()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupPaidCall_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupPaidCall_result)
lookupPaidCall_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaidCallResponse, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getExtendedProfile_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getExtendedProfile_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getExtendedProfile_args)
getExtendedProfile_args.thrift_spec = (
)


class getExtendedProfile_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = ExtendedProfile()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getExtendedProfile_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getExtendedProfile_result)
getExtendedProfile_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [ExtendedProfile, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getReverseCompactContacts_args(object):
    """
    Attributes:
     - ids
    """


    def __init__(self, ids=None,):
        self.ids = ids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.ids = []
                    (_etype2275, _size2272) = iprot.readListBegin()
                    for _i2276 in range(_size2272):
                        _elem2277 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.ids.append(_elem2277)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getReverseCompactContacts_args')
        if self.ids is not None:
            oprot.writeFieldBegin('ids', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.ids))
            for iter2278 in self.ids:
                oprot.writeString(iter2278.encode('utf-8') if sys.version_info[0] == 2 else iter2278)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getReverseCompactContacts_args)
getReverseCompactContacts_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'ids', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class getReverseCompactContacts_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.MAP:
                    self.success = {}
                    (_ktype2280, _vtype2281, _size2279) = iprot.readMapBegin()
                    for _i2283 in range(_size2279):
                        _key2284 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val2285 = CompactContact()
                        _val2285.read(iprot)
                        self.success[_key2284] = _val2285
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getReverseCompactContacts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.success))
            for kiter2286, viter2287 in self.success.items():
                oprot.writeString(kiter2286.encode('utf-8') if sys.version_info[0] == 2 else kiter2286)
                viter2287.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getReverseCompactContacts_result)
getReverseCompactContacts_result.thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING, 'UTF8', TType.STRUCT, [CompactContact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPaidCallAdStatus_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallAdStatus_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallAdStatus_args)
getPaidCallAdStatus_args.thrift_spec = (
)


class getPaidCallAdStatus_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = PaidCallAdResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getPaidCallAdStatus_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getPaidCallAdStatus_result)
getPaidCallAdStatus_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [PaidCallAdResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class findContactByUseridWithoutAbuseBlockForChannel_args(object):
    """
    Attributes:
     - userid
    """


    def __init__(self, userid=None,):
        self.userid = userid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.userid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('findContactByUseridWithoutAbuseBlockForChannel_args')
        if self.userid is not None:
            oprot.writeFieldBegin('userid', TType.STRING, 2)
            oprot.writeString(self.userid.encode('utf-8') if sys.version_info[0] == 2 else self.userid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(findContactByUseridWithoutAbuseBlockForChannel_args)
findContactByUseridWithoutAbuseBlockForChannel_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'userid', 'UTF8', None, ),  # 2
)


class findContactByUseridWithoutAbuseBlockForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Contact()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('findContactByUseridWithoutAbuseBlockForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(findContactByUseridWithoutAbuseBlockForChannel_result)
findContactByUseridWithoutAbuseBlockForChannel_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Contact, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getGroupMemberMids_args(object):
    """
    Attributes:
     - groupId
    """


    def __init__(self, groupId=None,):
        self.groupId = groupId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.groupId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupMemberMids_args')
        if self.groupId is not None:
            oprot.writeFieldBegin('groupId', TType.STRING, 1)
            oprot.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupMemberMids_args)
getGroupMemberMids_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'groupId', 'UTF8', None, ),  # 1
)


class getGroupMemberMids_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2291, _size2288) = iprot.readListBegin()
                    for _i2292 in range(_size2288):
                        _elem2293 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2293)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getGroupMemberMids_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2294 in self.success:
                oprot.writeString(iter2294.encode('utf-8') if sys.version_info[0] == 2 else iter2294)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getGroupMemberMids_result)
getGroupMemberMids_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendMessageWithoutRelationship_args(object):
    """
    Attributes:
     - message
    """


    def __init__(self, message=None,):
        self.message = message

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.message = Message()
                    self.message.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendMessageWithoutRelationship_args')
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRUCT, 2)
            self.message.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendMessageWithoutRelationship_args)
sendMessageWithoutRelationship_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'message', [Message, None], None, ),  # 2
)


class sendMessageWithoutRelationship_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Message()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('sendMessageWithoutRelationship_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(sendMessageWithoutRelationship_result)
sendMessageWithoutRelationship_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Message, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class displayBuddySubscriberCountInBulk_args(object):
    """
    Attributes:
     - mids
    """


    def __init__(self, mids=None,):
        self.mids = mids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype2298, _size2295) = iprot.readListBegin()
                    for _i2299 in range(_size2295):
                        _elem2300 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem2300)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('displayBuddySubscriberCountInBulk_args')
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter2301 in self.mids:
                oprot.writeString(iter2301.encode('utf-8') if sys.version_info[0] == 2 else iter2301)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(displayBuddySubscriberCountInBulk_args)
displayBuddySubscriberCountInBulk_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class displayBuddySubscriberCountInBulk_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.MAP:
                    self.success = {}
                    (_ktype2303, _vtype2304, _size2302) = iprot.readMapBegin()
                    for _i2306 in range(_size2302):
                        _key2307 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val2308 = iprot.readI64()
                        self.success[_key2307] = _val2308
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('displayBuddySubscriberCountInBulk_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.STRING, TType.I64, len(self.success))
            for kiter2309, viter2310 in self.success.items():
                oprot.writeString(kiter2309.encode('utf-8') if sys.version_info[0] == 2 else kiter2309)
                oprot.writeI64(viter2310)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(displayBuddySubscriberCountInBulk_result)
displayBuddySubscriberCountInBulk_result.thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING, 'UTF8', TType.I64, None, False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class lookupRoomMembers_args(object):
    """
    Attributes:
     - roomId
     - mids
    """


    def __init__(self, roomId=None, mids=None,):
        self.roomId = roomId
        self.mids = mids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.roomId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype2314, _size2311) = iprot.readListBegin()
                    for _i2315 in range(_size2311):
                        _elem2316 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem2316)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupRoomMembers_args')
        if self.roomId is not None:
            oprot.writeFieldBegin('roomId', TType.STRING, 1)
            oprot.writeString(self.roomId.encode('utf-8') if sys.version_info[0] == 2 else self.roomId)
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter2317 in self.mids:
                oprot.writeString(iter2317.encode('utf-8') if sys.version_info[0] == 2 else iter2317)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupRoomMembers_args)
lookupRoomMembers_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'roomId', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 2
)


class lookupRoomMembers_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2321, _size2318) = iprot.readListBegin()
                    for _i2322 in range(_size2318):
                        _elem2323 = SimpleChannelContact()
                        _elem2323.read(iprot)
                        self.success.append(_elem2323)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('lookupRoomMembers_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2324 in self.success:
                iter2324.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(lookupRoomMembers_result)
lookupRoomMembers_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [SimpleChannelContact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getFavoriteMidsForChannel_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFavoriteMidsForChannel_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFavoriteMidsForChannel_args)
getFavoriteMidsForChannel_args.thrift_spec = (
)


class getFavoriteMidsForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2328, _size2325) = iprot.readListBegin()
                    for _i2329 in range(_size2325):
                        _elem2330 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2330)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getFavoriteMidsForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2331 in self.success:
                oprot.writeString(iter2331.encode('utf-8') if sys.version_info[0] == 2 else iter2331)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getFavoriteMidsForChannel_result)
getFavoriteMidsForChannel_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getAllContactIdsForChannel_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getAllContactIdsForChannel_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getAllContactIdsForChannel_args)
getAllContactIdsForChannel_args.thrift_spec = (
)


class getAllContactIdsForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2335, _size2332) = iprot.readListBegin()
                    for _i2336 in range(_size2332):
                        _elem2337 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2337)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getAllContactIdsForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2338 in self.success:
                oprot.writeString(iter2338.encode('utf-8') if sys.version_info[0] == 2 else iter2338)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getAllContactIdsForChannel_result)
getAllContactIdsForChannel_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class displayBuddySubscriberCount_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('displayBuddySubscriberCount_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(displayBuddySubscriberCount_args)
displayBuddySubscriberCount_args.thrift_spec = (
)


class displayBuddySubscriberCount_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('displayBuddySubscriberCount_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(displayBuddySubscriberCount_result)
displayBuddySubscriberCount_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getProfileForChannel_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProfileForChannel_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getProfileForChannel_args)
getProfileForChannel_args.thrift_spec = (
)


class getProfileForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Profile()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getProfileForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getProfileForChannel_result)
getProfileForChannel_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Profile, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUserTickets_args(object):
    """
    Attributes:
     - userMids
    """


    def __init__(self, userMids=None,):
        self.userMids = userMids

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.userMids = []
                    (_etype2342, _size2339) = iprot.readListBegin()
                    for _i2343 in range(_size2339):
                        _elem2344 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.userMids.append(_elem2344)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserTickets_args')
        if self.userMids is not None:
            oprot.writeFieldBegin('userMids', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.userMids))
            for iter2345 in self.userMids:
                oprot.writeString(iter2345.encode('utf-8') if sys.version_info[0] == 2 else iter2345)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserTickets_args)
getUserTickets_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'userMids', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class getUserTickets_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2349, _size2346) = iprot.readListBegin()
                    for _i2350 in range(_size2346):
                        _elem2351 = UserTicketResponse()
                        _elem2351.read(iprot)
                        self.success.append(_elem2351)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserTickets_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2352 in self.success:
                iter2352.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserTickets_result)
getUserTickets_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [UserTicketResponse, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getOAFriendMids_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getOAFriendMids_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getOAFriendMids_args)
getOAFriendMids_args.thrift_spec = (
)


class getOAFriendMids_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2356, _size2353) = iprot.readListBegin()
                    for _i2357 in range(_size2353):
                        _elem2358 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2358)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getOAFriendMids_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2359 in self.success:
                oprot.writeString(iter2359.encode('utf-8') if sys.version_info[0] == 2 else iter2359)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getOAFriendMids_result)
getOAFriendMids_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class searchPaidCallUserRate_args(object):
    """
    Attributes:
     - countryCode
     - language
    """


    def __init__(self, countryCode=None, language=None,):
        self.countryCode = countryCode
        self.language = language

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.countryCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('searchPaidCallUserRate_args')
        if self.countryCode is not None:
            oprot.writeFieldBegin('countryCode', TType.STRING, 2)
            oprot.writeString(self.countryCode.encode('utf-8') if sys.version_info[0] == 2 else self.countryCode)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 3)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(searchPaidCallUserRate_args)
searchPaidCallUserRate_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'countryCode', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'language', 'UTF8', None, ),  # 3
)


class searchPaidCallUserRate_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2363, _size2360) = iprot.readListBegin()
                    for _i2364 in range(_size2360):
                        _elem2365 = PaidCallUserRate()
                        _elem2365.read(iprot)
                        self.success.append(_elem2365)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('searchPaidCallUserRate_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2366 in self.success:
                iter2366.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(searchPaidCallUserRate_result)
searchPaidCallUserRate_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [PaidCallUserRate, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getJoinedGroupIdsForChannel_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getJoinedGroupIdsForChannel_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getJoinedGroupIdsForChannel_args)
getJoinedGroupIdsForChannel_args.thrift_spec = (
)


class getJoinedGroupIdsForChannel_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2370, _size2367) = iprot.readListBegin()
                    for _i2371 in range(_size2367):
                        _elem2372 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2372)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getJoinedGroupIdsForChannel_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2373 in self.success:
                oprot.writeString(iter2373.encode('utf-8') if sys.version_info[0] == 2 else iter2373)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getJoinedGroupIdsForChannel_result)
getJoinedGroupIdsForChannel_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class acquireGroupCallRoute_args(object):
    """
    Attributes:
     - chatMid
     - mediaType
    """


    def __init__(self, chatMid=None, mediaType=None,):
        self.chatMid = chatMid
        self.mediaType = mediaType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.chatMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.mediaType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('acquireGroupCallRoute_args')
        if self.chatMid is not None:
            oprot.writeFieldBegin('chatMid', TType.STRING, 2)
            oprot.writeString(self.chatMid.encode('utf-8') if sys.version_info[0] == 2 else self.chatMid)
            oprot.writeFieldEnd()
        if self.mediaType is not None:
            oprot.writeFieldBegin('mediaType', TType.I32, 3)
            oprot.writeI32(self.mediaType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(acquireGroupCallRoute_args)
acquireGroupCallRoute_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'chatMid', 'UTF8', None, ),  # 2
    (3, TType.I32, 'mediaType', None, None, ),  # 3
)


class acquireGroupCallRoute_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = GroupCallRoute()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('acquireGroupCallRoute_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(acquireGroupCallRoute_result)
acquireGroupCallRoute_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [GroupCallRoute, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUserMidsWhoAddedMe_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserMidsWhoAddedMe_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserMidsWhoAddedMe_args)
getUserMidsWhoAddedMe_args.thrift_spec = (
)


class getUserMidsWhoAddedMe_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2377, _size2374) = iprot.readListBegin()
                    for _i2378 in range(_size2374):
                        _elem2379 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem2379)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserMidsWhoAddedMe_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter2380 in self.success:
                oprot.writeString(iter2380.encode('utf-8') if sys.version_info[0] == 2 else iter2380)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserMidsWhoAddedMe_result)
getUserMidsWhoAddedMe_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getIdentityCredential_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getIdentityCredential_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getIdentityCredential_args)
getIdentityCredential_args.thrift_spec = (
)


class getIdentityCredential_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = IdentityCredential()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getIdentityCredential_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getIdentityCredential_result)
getIdentityCredential_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [IdentityCredential, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class addOperationForChannel_args(object):
    """
    Attributes:
     - opType
     - param1
     - param2
     - param3
    """


    def __init__(self, opType=None, param1=None, param2=None, param3=None,):
        self.opType = opType
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.opType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.param1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.param2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.param3 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('addOperationForChannel_args')
        if self.opType is not None:
            oprot.writeFieldBegin('opType', TType.I32, 1)
            oprot.writeI32(self.opType)
            oprot.writeFieldEnd()
        if self.param1 is not None:
            oprot.writeFieldBegin('param1', TType.STRING, 2)
            oprot.writeString(self.param1.encode('utf-8') if sys.version_info[0] == 2 else self.param1)
            oprot.writeFieldEnd()
        if self.param2 is not None:
            oprot.writeFieldBegin('param2', TType.STRING, 3)
            oprot.writeString(self.param2.encode('utf-8') if sys.version_info[0] == 2 else self.param2)
            oprot.writeFieldEnd()
        if self.param3 is not None:
            oprot.writeFieldBegin('param3', TType.STRING, 4)
            oprot.writeString(self.param3.encode('utf-8') if sys.version_info[0] == 2 else self.param3)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(addOperationForChannel_args)
addOperationForChannel_args.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'opType', None, None, ),  # 1
    (2, TType.STRING, 'param1', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'param2', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'param3', 'UTF8', None, ),  # 4
)


class addOperationForChannel_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('addOperationForChannel_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(addOperationForChannel_result)
addOperationForChannel_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getSimpleChannelContacts_args(object):
    """
    Attributes:
     - ids
     - statusSticonFallbackDisabled
    """


    def __init__(self, ids=None, statusSticonFallbackDisabled=None,):
        self.ids = ids
        self.statusSticonFallbackDisabled = statusSticonFallbackDisabled

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.ids = []
                    (_etype2384, _size2381) = iprot.readListBegin()
                    for _i2385 in range(_size2381):
                        _elem2386 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.ids.append(_elem2386)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.statusSticonFallbackDisabled = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getSimpleChannelContacts_args')
        if self.ids is not None:
            oprot.writeFieldBegin('ids', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.ids))
            for iter2387 in self.ids:
                oprot.writeString(iter2387.encode('utf-8') if sys.version_info[0] == 2 else iter2387)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.statusSticonFallbackDisabled is not None:
            oprot.writeFieldBegin('statusSticonFallbackDisabled', TType.BOOL, 2)
            oprot.writeBool(self.statusSticonFallbackDisabled)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getSimpleChannelContacts_args)
getSimpleChannelContacts_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'ids', (TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.BOOL, 'statusSticonFallbackDisabled', None, None, ),  # 2
)


class getSimpleChannelContacts_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype2391, _size2388) = iprot.readListBegin()
                    for _i2392 in range(_size2388):
                        _elem2393 = SimpleChannelContact()
                        _elem2393.read(iprot)
                        self.success.append(_elem2393)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getSimpleChannelContacts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter2394 in self.success:
                iter2394.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getSimpleChannelContacts_result)
getSimpleChannelContacts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [SimpleChannelContact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUserLastSentMessageTimeStamp_args(object):
    """
    Attributes:
     - mid
    """


    def __init__(self, mid=None,):
        self.mid = mid

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserLastSentMessageTimeStamp_args')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserLastSentMessageTimeStamp_args)
getUserLastSentMessageTimeStamp_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
)


class getUserLastSentMessageTimeStamp_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('getUserLastSentMessageTimeStamp_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(getUserLastSentMessageTimeStamp_result)
getUserLastSentMessageTimeStamp_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
#fix_spec(all_structs)
del all_structs

