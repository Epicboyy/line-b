from ..ThriftService import *
import sys
import logging
from .ttypes import *

all_structs = []


class Iface(object):
    def addBuddyMember(self, requestId, userMid):
        """
        Parameters:
         - requestId
         - userMid
        """
        pass

    def addBuddyMembers(self, requestId, userMids):
        """
        Parameters:
         - requestId
         - userMids
        """
        pass

    def blockBuddyMember(self, requestId, mid):
        """
        Parameters:
         - requestId
         - mid
        """
        pass

    def commitSendMessagesToAll(self, requestIdList):
        """
        Parameters:
         - requestIdList
        """
        pass

    def commitSendMessagesToMids(self, requestIdList, mids):
        """
        Parameters:
         - requestIdList
         - mids
        """
        pass

    def containsBuddyMember(self, requestId, userMid):
        """
        Parameters:
         - requestId
         - userMid
        """
        pass

    def downloadMessageContent(self, requestId, messageId):
        """
        Parameters:
         - requestId
         - messageId
        """
        pass

    def downloadMessageContentPreview(self, requestId, messageId):
        """
        Parameters:
         - requestId
         - messageId
        """
        pass

    def downloadProfileImage(self, requestId):
        """
        Parameters:
         - requestId
        """
        pass

    def downloadProfileImagePreview(self, requestId):
        """
        Parameters:
         - requestId
        """
        pass

    def getActiveMemberCountByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getActiveMemberMidsByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getAllBuddyMembers(self):
        pass

    def getBlockedBuddyMembers(self):
        pass

    def getBlockerCountByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getBuddyDetailByMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getBuddyProfile(self):
        pass

    def getContactTicket(self):
        pass

    def getMemberCountByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getSendBuddyMessageResult(self, sendBuddyMessageRequestId):
        """
        Parameters:
         - sendBuddyMessageRequestId
        """
        pass

    def getSetBuddyOnAirResult(self, setBuddyOnAirRequestId):
        """
        Parameters:
         - setBuddyOnAirRequestId
        """
        pass

    def getUpdateBuddyProfileResult(self, updateBuddyProfileRequestId):
        """
        Parameters:
         - updateBuddyProfileRequestId
        """
        pass

    def isBuddyOnAirByMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def linkAndSendBuddyContentMessageToAllAsync(self, requestId, msg, sourceContentId):
        """
        Parameters:
         - requestId
         - msg
         - sourceContentId
        """
        pass

    def linkAndSendBuddyContentMessageToMids(self, requestId, msg, sourceContentId, mids):
        """
        Parameters:
         - requestId
         - msg
         - sourceContentId
         - mids
        """
        pass

    def notifyBuddyBlocked(self, buddyMid, blockerMid):
        """
        Parameters:
         - buddyMid
         - blockerMid
        """
        pass

    def notifyBuddyUnblocked(self, buddyMid, blockerMid):
        """
        Parameters:
         - buddyMid
         - blockerMid
        """
        pass

    def registerBuddy(self, buddyId, searchId, displayName, statusMeessage, picture, settings):
        """
        Parameters:
         - buddyId
         - searchId
         - displayName
         - statusMeessage
         - picture
         - settings
        """
        pass

    def registerBuddyAdmin(self, buddyId, searchId, displayName, statusMessage, picture):
        """
        Parameters:
         - buddyId
         - searchId
         - displayName
         - statusMessage
         - picture
        """
        pass

    def reissueContactTicket(self, expirationTime, maxUseCount):
        """
        Parameters:
         - expirationTime
         - maxUseCount
        """
        pass

    def removeBuddyMember(self, requestId, userMid):
        """
        Parameters:
         - requestId
         - userMid
        """
        pass

    def removeBuddyMembers(self, requestId, userMids):
        """
        Parameters:
         - requestId
         - userMids
        """
        pass

    def sendBuddyContentMessageToAll(self, requestId, msg, content):
        """
        Parameters:
         - requestId
         - msg
         - content
        """
        pass

    def sendBuddyContentMessageToAllAsync(self, requestId, msg, content):
        """
        Parameters:
         - requestId
         - msg
         - content
        """
        pass

    def sendBuddyContentMessageToMids(self, requestId, msg, content, mids):
        """
        Parameters:
         - requestId
         - msg
         - content
         - mids
        """
        pass

    def sendBuddyContentMessageToMidsAsync(self, requestId, msg, content, mids):
        """
        Parameters:
         - requestId
         - msg
         - content
         - mids
        """
        pass

    def sendBuddyMessageToAll(self, requestId, msg):
        """
        Parameters:
         - requestId
         - msg
        """
        pass

    def sendBuddyMessageToAllAsync(self, requestId, msg):
        """
        Parameters:
         - requestId
         - msg
        """
        pass

    def sendBuddyMessageToMids(self, requestId, msg, mids):
        """
        Parameters:
         - requestId
         - msg
         - mids
        """
        pass

    def sendBuddyMessageToMidsAsync(self, requestId, msg, mids):
        """
        Parameters:
         - requestId
         - msg
         - mids
        """
        pass

    def sendIndividualEventToAllAsync(self, requestId, buddyMid, notificationStatus):
        """
        Parameters:
         - requestId
         - buddyMid
         - notificationStatus
        """
        pass

    def setBuddyOnAir(self, requestId, onAir):
        """
        Parameters:
         - requestId
         - onAir
        """
        pass

    def setBuddyOnAirAsync(self, requestId, onAir):
        """
        Parameters:
         - requestId
         - onAir
        """
        pass

    def storeMessage(self, requestId, messageRequest):
        """
        Parameters:
         - requestId
         - messageRequest
        """
        pass

    def unblockBuddyMember(self, requestId, mid):
        """
        Parameters:
         - requestId
         - mid
        """
        pass

    def unregisterBuddy(self, requestId):
        """
        Parameters:
         - requestId
        """
        pass

    def unregisterBuddyAdmin(self, requestId):
        """
        Parameters:
         - requestId
        """
        pass

    def updateBuddyAdminProfileAttribute(self, requestId, attributes):
        """
        Parameters:
         - requestId
         - attributes
        """
        pass

    def updateBuddyAdminProfileImage(self, requestId, picture):
        """
        Parameters:
         - requestId
         - picture
        """
        pass

    def updateBuddyProfileAttributes(self, requestId, attributes):
        """
        Parameters:
         - requestId
         - attributes
        """
        pass

    def updateBuddyProfileAttributesAsync(self, requestId, attributes):
        """
        Parameters:
         - requestId
         - attributes
        """
        pass

    def updateBuddyProfileImage(self, requestId, image):
        """
        Parameters:
         - requestId
         - image
        """
        pass

    def updateBuddyProfileImageAsync(self, requestId, image):
        """
        Parameters:
         - requestId
         - image
        """
        pass

    def updateBuddySearchId(self, requestId, searchId):
        """
        Parameters:
         - requestId
         - searchId
        """
        pass

    def updateBuddySettings(self, settings):
        """
        Parameters:
         - settings
        """
        pass

    def uploadBuddyContent(self, contentType, content):
        """
        Parameters:
         - contentType
         - content
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def addBuddyMember(self, requestId, userMid):
        """
        Parameters:
         - requestId
         - userMid
        """
        self.send_addBuddyMember(requestId, userMid)
        self.recv_addBuddyMember()

    def send_addBuddyMember(self, requestId, userMid):
        self._oprot.writeMessageBegin('addBuddyMember', TMessageType.CALL, self._seqid)
        args = addBuddyMember_args()
        args.requestId = requestId
        args.userMid = userMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_addBuddyMember(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = addBuddyMember_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def addBuddyMembers(self, requestId, userMids):
        """
        Parameters:
         - requestId
         - userMids
        """
        self.send_addBuddyMembers(requestId, userMids)
        self.recv_addBuddyMembers()

    def send_addBuddyMembers(self, requestId, userMids):
        self._oprot.writeMessageBegin('addBuddyMembers', TMessageType.CALL, self._seqid)
        args = addBuddyMembers_args()
        args.requestId = requestId
        args.userMids = userMids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_addBuddyMembers(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = addBuddyMembers_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def blockBuddyMember(self, requestId, mid):
        """
        Parameters:
         - requestId
         - mid
        """
        self.send_blockBuddyMember(requestId, mid)
        self.recv_blockBuddyMember()

    def send_blockBuddyMember(self, requestId, mid):
        self._oprot.writeMessageBegin('blockBuddyMember', TMessageType.CALL, self._seqid)
        args = blockBuddyMember_args()
        args.requestId = requestId
        args.mid = mid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_blockBuddyMember(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = blockBuddyMember_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def commitSendMessagesToAll(self, requestIdList):
        """
        Parameters:
         - requestIdList
        """
        self.send_commitSendMessagesToAll(requestIdList)
        return self.recv_commitSendMessagesToAll()

    def send_commitSendMessagesToAll(self, requestIdList):
        self._oprot.writeMessageBegin('commitSendMessagesToAll', TMessageType.CALL, self._seqid)
        args = commitSendMessagesToAll_args()
        args.requestIdList = requestIdList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_commitSendMessagesToAll(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = commitSendMessagesToAll_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "commitSendMessagesToAll failed: unknown result")

    def commitSendMessagesToMids(self, requestIdList, mids):
        """
        Parameters:
         - requestIdList
         - mids
        """
        self.send_commitSendMessagesToMids(requestIdList, mids)
        return self.recv_commitSendMessagesToMids()

    def send_commitSendMessagesToMids(self, requestIdList, mids):
        self._oprot.writeMessageBegin('commitSendMessagesToMids', TMessageType.CALL, self._seqid)
        args = commitSendMessagesToMids_args()
        args.requestIdList = requestIdList
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_commitSendMessagesToMids(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = commitSendMessagesToMids_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "commitSendMessagesToMids failed: unknown result")

    def containsBuddyMember(self, requestId, userMid):
        """
        Parameters:
         - requestId
         - userMid
        """
        self.send_containsBuddyMember(requestId, userMid)
        return self.recv_containsBuddyMember()

    def send_containsBuddyMember(self, requestId, userMid):
        self._oprot.writeMessageBegin('containsBuddyMember', TMessageType.CALL, self._seqid)
        args = containsBuddyMember_args()
        args.requestId = requestId
        args.userMid = userMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_containsBuddyMember(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = containsBuddyMember_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "containsBuddyMember failed: unknown result")

    def downloadMessageContent(self, requestId, messageId):
        """
        Parameters:
         - requestId
         - messageId
        """
        self.send_downloadMessageContent(requestId, messageId)
        return self.recv_downloadMessageContent()

    def send_downloadMessageContent(self, requestId, messageId):
        self._oprot.writeMessageBegin('downloadMessageContent', TMessageType.CALL, self._seqid)
        args = downloadMessageContent_args()
        args.requestId = requestId
        args.messageId = messageId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_downloadMessageContent(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = downloadMessageContent_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "downloadMessageContent failed: unknown result")

    def downloadMessageContentPreview(self, requestId, messageId):
        """
        Parameters:
         - requestId
         - messageId
        """
        self.send_downloadMessageContentPreview(requestId, messageId)
        return self.recv_downloadMessageContentPreview()

    def send_downloadMessageContentPreview(self, requestId, messageId):
        self._oprot.writeMessageBegin('downloadMessageContentPreview', TMessageType.CALL, self._seqid)
        args = downloadMessageContentPreview_args()
        args.requestId = requestId
        args.messageId = messageId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_downloadMessageContentPreview(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = downloadMessageContentPreview_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "downloadMessageContentPreview failed: unknown result")

    def downloadProfileImage(self, requestId):
        """
        Parameters:
         - requestId
        """
        self.send_downloadProfileImage(requestId)
        return self.recv_downloadProfileImage()

    def send_downloadProfileImage(self, requestId):
        self._oprot.writeMessageBegin('downloadProfileImage', TMessageType.CALL, self._seqid)
        args = downloadProfileImage_args()
        args.requestId = requestId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_downloadProfileImage(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = downloadProfileImage_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "downloadProfileImage failed: unknown result")

    def downloadProfileImagePreview(self, requestId):
        """
        Parameters:
         - requestId
        """
        self.send_downloadProfileImagePreview(requestId)
        return self.recv_downloadProfileImagePreview()

    def send_downloadProfileImagePreview(self, requestId):
        self._oprot.writeMessageBegin('downloadProfileImagePreview', TMessageType.CALL, self._seqid)
        args = downloadProfileImagePreview_args()
        args.requestId = requestId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_downloadProfileImagePreview(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = downloadProfileImagePreview_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "downloadProfileImagePreview failed: unknown result")

    def getActiveMemberCountByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_getActiveMemberCountByBuddyMid(buddyMid)
        return self.recv_getActiveMemberCountByBuddyMid()

    def send_getActiveMemberCountByBuddyMid(self, buddyMid):
        self._oprot.writeMessageBegin('getActiveMemberCountByBuddyMid', TMessageType.CALL, self._seqid)
        args = getActiveMemberCountByBuddyMid_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getActiveMemberCountByBuddyMid(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getActiveMemberCountByBuddyMid_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getActiveMemberCountByBuddyMid failed: unknown result")

    def getActiveMemberMidsByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_getActiveMemberMidsByBuddyMid(buddyMid)
        return self.recv_getActiveMemberMidsByBuddyMid()

    def send_getActiveMemberMidsByBuddyMid(self, buddyMid):
        self._oprot.writeMessageBegin('getActiveMemberMidsByBuddyMid', TMessageType.CALL, self._seqid)
        args = getActiveMemberMidsByBuddyMid_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getActiveMemberMidsByBuddyMid(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getActiveMemberMidsByBuddyMid_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getActiveMemberMidsByBuddyMid failed: unknown result")

    def getAllBuddyMembers(self):
        self.send_getAllBuddyMembers()
        return self.recv_getAllBuddyMembers()

    def send_getAllBuddyMembers(self):
        self._oprot.writeMessageBegin('getAllBuddyMembers', TMessageType.CALL, self._seqid)
        args = getAllBuddyMembers_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getAllBuddyMembers(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getAllBuddyMembers_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getAllBuddyMembers failed: unknown result")

    def getBlockedBuddyMembers(self):
        self.send_getBlockedBuddyMembers()
        return self.recv_getBlockedBuddyMembers()

    def send_getBlockedBuddyMembers(self):
        self._oprot.writeMessageBegin('getBlockedBuddyMembers', TMessageType.CALL, self._seqid)
        args = getBlockedBuddyMembers_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBlockedBuddyMembers(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBlockedBuddyMembers_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBlockedBuddyMembers failed: unknown result")

    def getBlockerCountByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_getBlockerCountByBuddyMid(buddyMid)
        return self.recv_getBlockerCountByBuddyMid()

    def send_getBlockerCountByBuddyMid(self, buddyMid):
        self._oprot.writeMessageBegin('getBlockerCountByBuddyMid', TMessageType.CALL, self._seqid)
        args = getBlockerCountByBuddyMid_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBlockerCountByBuddyMid(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBlockerCountByBuddyMid_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBlockerCountByBuddyMid failed: unknown result")

    def getBuddyDetailByMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_getBuddyDetailByMid(buddyMid)
        return self.recv_getBuddyDetailByMid()

    def send_getBuddyDetailByMid(self, buddyMid):
        self._oprot.writeMessageBegin('getBuddyDetailByMid', TMessageType.CALL, self._seqid)
        args = getBuddyDetailByMid_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBuddyDetailByMid(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBuddyDetailByMid_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBuddyDetailByMid failed: unknown result")

    def getBuddyProfile(self):
        self.send_getBuddyProfile()
        return self.recv_getBuddyProfile()

    def send_getBuddyProfile(self):
        self._oprot.writeMessageBegin('getBuddyProfile', TMessageType.CALL, self._seqid)
        args = getBuddyProfile_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBuddyProfile(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBuddyProfile_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBuddyProfile failed: unknown result")

    def getContactTicket(self):
        self.send_getContactTicket()
        return self.recv_getContactTicket()

    def send_getContactTicket(self):
        self._oprot.writeMessageBegin('getContactTicket', TMessageType.CALL, self._seqid)
        args = getContactTicket_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getContactTicket(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getContactTicket_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getContactTicket failed: unknown result")

    def getMemberCountByBuddyMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_getMemberCountByBuddyMid(buddyMid)
        return self.recv_getMemberCountByBuddyMid()

    def send_getMemberCountByBuddyMid(self, buddyMid):
        self._oprot.writeMessageBegin('getMemberCountByBuddyMid', TMessageType.CALL, self._seqid)
        args = getMemberCountByBuddyMid_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getMemberCountByBuddyMid(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getMemberCountByBuddyMid_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getMemberCountByBuddyMid failed: unknown result")

    def getSendBuddyMessageResult(self, sendBuddyMessageRequestId):
        """
        Parameters:
         - sendBuddyMessageRequestId
        """
        self.send_getSendBuddyMessageResult(sendBuddyMessageRequestId)
        return self.recv_getSendBuddyMessageResult()

    def send_getSendBuddyMessageResult(self, sendBuddyMessageRequestId):
        self._oprot.writeMessageBegin('getSendBuddyMessageResult', TMessageType.CALL, self._seqid)
        args = getSendBuddyMessageResult_args()
        args.sendBuddyMessageRequestId = sendBuddyMessageRequestId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getSendBuddyMessageResult(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getSendBuddyMessageResult_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getSendBuddyMessageResult failed: unknown result")

    def getSetBuddyOnAirResult(self, setBuddyOnAirRequestId):
        """
        Parameters:
         - setBuddyOnAirRequestId
        """
        self.send_getSetBuddyOnAirResult(setBuddyOnAirRequestId)
        return self.recv_getSetBuddyOnAirResult()

    def send_getSetBuddyOnAirResult(self, setBuddyOnAirRequestId):
        self._oprot.writeMessageBegin('getSetBuddyOnAirResult', TMessageType.CALL, self._seqid)
        args = getSetBuddyOnAirResult_args()
        args.setBuddyOnAirRequestId = setBuddyOnAirRequestId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getSetBuddyOnAirResult(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getSetBuddyOnAirResult_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getSetBuddyOnAirResult failed: unknown result")

    def getUpdateBuddyProfileResult(self, updateBuddyProfileRequestId):
        """
        Parameters:
         - updateBuddyProfileRequestId
        """
        self.send_getUpdateBuddyProfileResult(updateBuddyProfileRequestId)
        return self.recv_getUpdateBuddyProfileResult()

    def send_getUpdateBuddyProfileResult(self, updateBuddyProfileRequestId):
        self._oprot.writeMessageBegin('getUpdateBuddyProfileResult', TMessageType.CALL, self._seqid)
        args = getUpdateBuddyProfileResult_args()
        args.updateBuddyProfileRequestId = updateBuddyProfileRequestId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getUpdateBuddyProfileResult(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getUpdateBuddyProfileResult_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getUpdateBuddyProfileResult failed: unknown result")

    def isBuddyOnAirByMid(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_isBuddyOnAirByMid(buddyMid)
        return self.recv_isBuddyOnAirByMid()

    def send_isBuddyOnAirByMid(self, buddyMid):
        self._oprot.writeMessageBegin('isBuddyOnAirByMid', TMessageType.CALL, self._seqid)
        args = isBuddyOnAirByMid_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_isBuddyOnAirByMid(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = isBuddyOnAirByMid_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "isBuddyOnAirByMid failed: unknown result")

    def linkAndSendBuddyContentMessageToAllAsync(self, requestId, msg, sourceContentId):
        """
        Parameters:
         - requestId
         - msg
         - sourceContentId
        """
        self.send_linkAndSendBuddyContentMessageToAllAsync(requestId, msg, sourceContentId)
        return self.recv_linkAndSendBuddyContentMessageToAllAsync()

    def send_linkAndSendBuddyContentMessageToAllAsync(self, requestId, msg, sourceContentId):
        self._oprot.writeMessageBegin('linkAndSendBuddyContentMessageToAllAsync', TMessageType.CALL, self._seqid)
        args = linkAndSendBuddyContentMessageToAllAsync_args()
        args.requestId = requestId
        args.msg = msg
        args.sourceContentId = sourceContentId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_linkAndSendBuddyContentMessageToAllAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = linkAndSendBuddyContentMessageToAllAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "linkAndSendBuddyContentMessageToAllAsync failed: unknown result")

    def linkAndSendBuddyContentMessageToMids(self, requestId, msg, sourceContentId, mids):
        """
        Parameters:
         - requestId
         - msg
         - sourceContentId
         - mids
        """
        self.send_linkAndSendBuddyContentMessageToMids(requestId, msg, sourceContentId, mids)
        return self.recv_linkAndSendBuddyContentMessageToMids()

    def send_linkAndSendBuddyContentMessageToMids(self, requestId, msg, sourceContentId, mids):
        self._oprot.writeMessageBegin('linkAndSendBuddyContentMessageToMids', TMessageType.CALL, self._seqid)
        args = linkAndSendBuddyContentMessageToMids_args()
        args.requestId = requestId
        args.msg = msg
        args.sourceContentId = sourceContentId
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_linkAndSendBuddyContentMessageToMids(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = linkAndSendBuddyContentMessageToMids_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "linkAndSendBuddyContentMessageToMids failed: unknown result")

    def notifyBuddyBlocked(self, buddyMid, blockerMid):
        """
        Parameters:
         - buddyMid
         - blockerMid
        """
        self.send_notifyBuddyBlocked(buddyMid, blockerMid)
        self.recv_notifyBuddyBlocked()

    def send_notifyBuddyBlocked(self, buddyMid, blockerMid):
        self._oprot.writeMessageBegin('notifyBuddyBlocked', TMessageType.CALL, self._seqid)
        args = notifyBuddyBlocked_args()
        args.buddyMid = buddyMid
        args.blockerMid = blockerMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_notifyBuddyBlocked(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyBuddyBlocked_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def notifyBuddyUnblocked(self, buddyMid, blockerMid):
        """
        Parameters:
         - buddyMid
         - blockerMid
        """
        self.send_notifyBuddyUnblocked(buddyMid, blockerMid)
        self.recv_notifyBuddyUnblocked()

    def send_notifyBuddyUnblocked(self, buddyMid, blockerMid):
        self._oprot.writeMessageBegin('notifyBuddyUnblocked', TMessageType.CALL, self._seqid)
        args = notifyBuddyUnblocked_args()
        args.buddyMid = buddyMid
        args.blockerMid = blockerMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_notifyBuddyUnblocked(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = notifyBuddyUnblocked_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def registerBuddy(self, buddyId, searchId, displayName, statusMeessage, picture, settings):
        """
        Parameters:
         - buddyId
         - searchId
         - displayName
         - statusMeessage
         - picture
         - settings
        """
        self.send_registerBuddy(buddyId, searchId, displayName, statusMeessage, picture, settings)
        return self.recv_registerBuddy()

    def send_registerBuddy(self, buddyId, searchId, displayName, statusMeessage, picture, settings):
        self._oprot.writeMessageBegin('registerBuddy', TMessageType.CALL, self._seqid)
        args = registerBuddy_args()
        args.buddyId = buddyId
        args.searchId = searchId
        args.displayName = displayName
        args.statusMeessage = statusMeessage
        args.picture = picture
        args.settings = settings
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_registerBuddy(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = registerBuddy_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "registerBuddy failed: unknown result")

    def registerBuddyAdmin(self, buddyId, searchId, displayName, statusMessage, picture):
        """
        Parameters:
         - buddyId
         - searchId
         - displayName
         - statusMessage
         - picture
        """
        self.send_registerBuddyAdmin(buddyId, searchId, displayName, statusMessage, picture)
        return self.recv_registerBuddyAdmin()

    def send_registerBuddyAdmin(self, buddyId, searchId, displayName, statusMessage, picture):
        self._oprot.writeMessageBegin('registerBuddyAdmin', TMessageType.CALL, self._seqid)
        args = registerBuddyAdmin_args()
        args.buddyId = buddyId
        args.searchId = searchId
        args.displayName = displayName
        args.statusMessage = statusMessage
        args.picture = picture
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_registerBuddyAdmin(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = registerBuddyAdmin_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "registerBuddyAdmin failed: unknown result")

    def reissueContactTicket(self, expirationTime, maxUseCount):
        """
        Parameters:
         - expirationTime
         - maxUseCount
        """
        self.send_reissueContactTicket(expirationTime, maxUseCount)
        return self.recv_reissueContactTicket()

    def send_reissueContactTicket(self, expirationTime, maxUseCount):
        self._oprot.writeMessageBegin('reissueContactTicket', TMessageType.CALL, self._seqid)
        args = reissueContactTicket_args()
        args.expirationTime = expirationTime
        args.maxUseCount = maxUseCount
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_reissueContactTicket(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = reissueContactTicket_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "reissueContactTicket failed: unknown result")

    def removeBuddyMember(self, requestId, userMid):
        """
        Parameters:
         - requestId
         - userMid
        """
        self.send_removeBuddyMember(requestId, userMid)
        self.recv_removeBuddyMember()

    def send_removeBuddyMember(self, requestId, userMid):
        self._oprot.writeMessageBegin('removeBuddyMember', TMessageType.CALL, self._seqid)
        args = removeBuddyMember_args()
        args.requestId = requestId
        args.userMid = userMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_removeBuddyMember(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = removeBuddyMember_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def removeBuddyMembers(self, requestId, userMids):
        """
        Parameters:
         - requestId
         - userMids
        """
        self.send_removeBuddyMembers(requestId, userMids)
        self.recv_removeBuddyMembers()

    def send_removeBuddyMembers(self, requestId, userMids):
        self._oprot.writeMessageBegin('removeBuddyMembers', TMessageType.CALL, self._seqid)
        args = removeBuddyMembers_args()
        args.requestId = requestId
        args.userMids = userMids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_removeBuddyMembers(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = removeBuddyMembers_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def sendBuddyContentMessageToAll(self, requestId, msg, content):
        """
        Parameters:
         - requestId
         - msg
         - content
        """
        self.send_sendBuddyContentMessageToAll(requestId, msg, content)
        return self.recv_sendBuddyContentMessageToAll()

    def send_sendBuddyContentMessageToAll(self, requestId, msg, content):
        self._oprot.writeMessageBegin('sendBuddyContentMessageToAll', TMessageType.CALL, self._seqid)
        args = sendBuddyContentMessageToAll_args()
        args.requestId = requestId
        args.msg = msg
        args.content = content
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyContentMessageToAll(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyContentMessageToAll_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyContentMessageToAll failed: unknown result")

    def sendBuddyContentMessageToAllAsync(self, requestId, msg, content):
        """
        Parameters:
         - requestId
         - msg
         - content
        """
        self.send_sendBuddyContentMessageToAllAsync(requestId, msg, content)
        return self.recv_sendBuddyContentMessageToAllAsync()

    def send_sendBuddyContentMessageToAllAsync(self, requestId, msg, content):
        self._oprot.writeMessageBegin('sendBuddyContentMessageToAllAsync', TMessageType.CALL, self._seqid)
        args = sendBuddyContentMessageToAllAsync_args()
        args.requestId = requestId
        args.msg = msg
        args.content = content
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyContentMessageToAllAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyContentMessageToAllAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyContentMessageToAllAsync failed: unknown result")

    def sendBuddyContentMessageToMids(self, requestId, msg, content, mids):
        """
        Parameters:
         - requestId
         - msg
         - content
         - mids
        """
        self.send_sendBuddyContentMessageToMids(requestId, msg, content, mids)
        return self.recv_sendBuddyContentMessageToMids()

    def send_sendBuddyContentMessageToMids(self, requestId, msg, content, mids):
        self._oprot.writeMessageBegin('sendBuddyContentMessageToMids', TMessageType.CALL, self._seqid)
        args = sendBuddyContentMessageToMids_args()
        args.requestId = requestId
        args.msg = msg
        args.content = content
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyContentMessageToMids(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyContentMessageToMids_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyContentMessageToMids failed: unknown result")

    def sendBuddyContentMessageToMidsAsync(self, requestId, msg, content, mids):
        """
        Parameters:
         - requestId
         - msg
         - content
         - mids
        """
        self.send_sendBuddyContentMessageToMidsAsync(requestId, msg, content, mids)
        return self.recv_sendBuddyContentMessageToMidsAsync()

    def send_sendBuddyContentMessageToMidsAsync(self, requestId, msg, content, mids):
        self._oprot.writeMessageBegin('sendBuddyContentMessageToMidsAsync', TMessageType.CALL, self._seqid)
        args = sendBuddyContentMessageToMidsAsync_args()
        args.requestId = requestId
        args.msg = msg
        args.content = content
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyContentMessageToMidsAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyContentMessageToMidsAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyContentMessageToMidsAsync failed: unknown result")

    def sendBuddyMessageToAll(self, requestId, msg):
        """
        Parameters:
         - requestId
         - msg
        """
        self.send_sendBuddyMessageToAll(requestId, msg)
        return self.recv_sendBuddyMessageToAll()

    def send_sendBuddyMessageToAll(self, requestId, msg):
        self._oprot.writeMessageBegin('sendBuddyMessageToAll', TMessageType.CALL, self._seqid)
        args = sendBuddyMessageToAll_args()
        args.requestId = requestId
        args.msg = msg
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyMessageToAll(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyMessageToAll_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyMessageToAll failed: unknown result")

    def sendBuddyMessageToAllAsync(self, requestId, msg):
        """
        Parameters:
         - requestId
         - msg
        """
        self.send_sendBuddyMessageToAllAsync(requestId, msg)
        return self.recv_sendBuddyMessageToAllAsync()

    def send_sendBuddyMessageToAllAsync(self, requestId, msg):
        self._oprot.writeMessageBegin('sendBuddyMessageToAllAsync', TMessageType.CALL, self._seqid)
        args = sendBuddyMessageToAllAsync_args()
        args.requestId = requestId
        args.msg = msg
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyMessageToAllAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyMessageToAllAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyMessageToAllAsync failed: unknown result")

    def sendBuddyMessageToMids(self, requestId, msg, mids):
        """
        Parameters:
         - requestId
         - msg
         - mids
        """
        self.send_sendBuddyMessageToMids(requestId, msg, mids)
        return self.recv_sendBuddyMessageToMids()

    def send_sendBuddyMessageToMids(self, requestId, msg, mids):
        self._oprot.writeMessageBegin('sendBuddyMessageToMids', TMessageType.CALL, self._seqid)
        args = sendBuddyMessageToMids_args()
        args.requestId = requestId
        args.msg = msg
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyMessageToMids(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyMessageToMids_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyMessageToMids failed: unknown result")

    def sendBuddyMessageToMidsAsync(self, requestId, msg, mids):
        """
        Parameters:
         - requestId
         - msg
         - mids
        """
        self.send_sendBuddyMessageToMidsAsync(requestId, msg, mids)
        return self.recv_sendBuddyMessageToMidsAsync()

    def send_sendBuddyMessageToMidsAsync(self, requestId, msg, mids):
        self._oprot.writeMessageBegin('sendBuddyMessageToMidsAsync', TMessageType.CALL, self._seqid)
        args = sendBuddyMessageToMidsAsync_args()
        args.requestId = requestId
        args.msg = msg
        args.mids = mids
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendBuddyMessageToMidsAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendBuddyMessageToMidsAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "sendBuddyMessageToMidsAsync failed: unknown result")

    def sendIndividualEventToAllAsync(self, requestId, buddyMid, notificationStatus):
        """
        Parameters:
         - requestId
         - buddyMid
         - notificationStatus
        """
        self.send_sendIndividualEventToAllAsync(requestId, buddyMid, notificationStatus)
        self.recv_sendIndividualEventToAllAsync()

    def send_sendIndividualEventToAllAsync(self, requestId, buddyMid, notificationStatus):
        self._oprot.writeMessageBegin('sendIndividualEventToAllAsync', TMessageType.CALL, self._seqid)
        args = sendIndividualEventToAllAsync_args()
        args.requestId = requestId
        args.buddyMid = buddyMid
        args.notificationStatus = notificationStatus
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_sendIndividualEventToAllAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = sendIndividualEventToAllAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def setBuddyOnAir(self, requestId, onAir):
        """
        Parameters:
         - requestId
         - onAir
        """
        self.send_setBuddyOnAir(requestId, onAir)
        return self.recv_setBuddyOnAir()

    def send_setBuddyOnAir(self, requestId, onAir):
        self._oprot.writeMessageBegin('setBuddyOnAir', TMessageType.CALL, self._seqid)
        args = setBuddyOnAir_args()
        args.requestId = requestId
        args.onAir = onAir
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_setBuddyOnAir(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = setBuddyOnAir_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "setBuddyOnAir failed: unknown result")

    def setBuddyOnAirAsync(self, requestId, onAir):
        """
        Parameters:
         - requestId
         - onAir
        """
        self.send_setBuddyOnAirAsync(requestId, onAir)
        return self.recv_setBuddyOnAirAsync()

    def send_setBuddyOnAirAsync(self, requestId, onAir):
        self._oprot.writeMessageBegin('setBuddyOnAirAsync', TMessageType.CALL, self._seqid)
        args = setBuddyOnAirAsync_args()
        args.requestId = requestId
        args.onAir = onAir
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_setBuddyOnAirAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = setBuddyOnAirAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "setBuddyOnAirAsync failed: unknown result")

    def storeMessage(self, requestId, messageRequest):
        """
        Parameters:
         - requestId
         - messageRequest
        """
        self.send_storeMessage(requestId, messageRequest)
        return self.recv_storeMessage()

    def send_storeMessage(self, requestId, messageRequest):
        self._oprot.writeMessageBegin('storeMessage', TMessageType.CALL, self._seqid)
        args = storeMessage_args()
        args.requestId = requestId
        args.messageRequest = messageRequest
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_storeMessage(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = storeMessage_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "storeMessage failed: unknown result")

    def unblockBuddyMember(self, requestId, mid):
        """
        Parameters:
         - requestId
         - mid
        """
        self.send_unblockBuddyMember(requestId, mid)
        self.recv_unblockBuddyMember()

    def send_unblockBuddyMember(self, requestId, mid):
        self._oprot.writeMessageBegin('unblockBuddyMember', TMessageType.CALL, self._seqid)
        args = unblockBuddyMember_args()
        args.requestId = requestId
        args.mid = mid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_unblockBuddyMember(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = unblockBuddyMember_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def unregisterBuddy(self, requestId):
        """
        Parameters:
         - requestId
        """
        self.send_unregisterBuddy(requestId)
        self.recv_unregisterBuddy()

    def send_unregisterBuddy(self, requestId):
        self._oprot.writeMessageBegin('unregisterBuddy', TMessageType.CALL, self._seqid)
        args = unregisterBuddy_args()
        args.requestId = requestId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_unregisterBuddy(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = unregisterBuddy_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def unregisterBuddyAdmin(self, requestId):
        """
        Parameters:
         - requestId
        """
        self.send_unregisterBuddyAdmin(requestId)
        self.recv_unregisterBuddyAdmin()

    def send_unregisterBuddyAdmin(self, requestId):
        self._oprot.writeMessageBegin('unregisterBuddyAdmin', TMessageType.CALL, self._seqid)
        args = unregisterBuddyAdmin_args()
        args.requestId = requestId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_unregisterBuddyAdmin(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = unregisterBuddyAdmin_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def updateBuddyAdminProfileAttribute(self, requestId, attributes):
        """
        Parameters:
         - requestId
         - attributes
        """
        self.send_updateBuddyAdminProfileAttribute(requestId, attributes)
        self.recv_updateBuddyAdminProfileAttribute()

    def send_updateBuddyAdminProfileAttribute(self, requestId, attributes):
        self._oprot.writeMessageBegin('updateBuddyAdminProfileAttribute', TMessageType.CALL, self._seqid)
        args = updateBuddyAdminProfileAttribute_args()
        args.requestId = requestId
        args.attributes = attributes
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddyAdminProfileAttribute(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddyAdminProfileAttribute_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def updateBuddyAdminProfileImage(self, requestId, picture):
        """
        Parameters:
         - requestId
         - picture
        """
        self.send_updateBuddyAdminProfileImage(requestId, picture)
        self.recv_updateBuddyAdminProfileImage()

    def send_updateBuddyAdminProfileImage(self, requestId, picture):
        self._oprot.writeMessageBegin('updateBuddyAdminProfileImage', TMessageType.CALL, self._seqid)
        args = updateBuddyAdminProfileImage_args()
        args.requestId = requestId
        args.picture = picture
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddyAdminProfileImage(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddyAdminProfileImage_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def updateBuddyProfileAttributes(self, requestId, attributes):
        """
        Parameters:
         - requestId
         - attributes
        """
        self.send_updateBuddyProfileAttributes(requestId, attributes)
        return self.recv_updateBuddyProfileAttributes()

    def send_updateBuddyProfileAttributes(self, requestId, attributes):
        self._oprot.writeMessageBegin('updateBuddyProfileAttributes', TMessageType.CALL, self._seqid)
        args = updateBuddyProfileAttributes_args()
        args.requestId = requestId
        args.attributes = attributes
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddyProfileAttributes(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddyProfileAttributes_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "updateBuddyProfileAttributes failed: unknown result")

    def updateBuddyProfileAttributesAsync(self, requestId, attributes):
        """
        Parameters:
         - requestId
         - attributes
        """
        self.send_updateBuddyProfileAttributesAsync(requestId, attributes)
        return self.recv_updateBuddyProfileAttributesAsync()

    def send_updateBuddyProfileAttributesAsync(self, requestId, attributes):
        self._oprot.writeMessageBegin('updateBuddyProfileAttributesAsync', TMessageType.CALL, self._seqid)
        args = updateBuddyProfileAttributesAsync_args()
        args.requestId = requestId
        args.attributes = attributes
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddyProfileAttributesAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddyProfileAttributesAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "updateBuddyProfileAttributesAsync failed: unknown result")

    def updateBuddyProfileImage(self, requestId, image):
        """
        Parameters:
         - requestId
         - image
        """
        self.send_updateBuddyProfileImage(requestId, image)
        return self.recv_updateBuddyProfileImage()

    def send_updateBuddyProfileImage(self, requestId, image):
        self._oprot.writeMessageBegin('updateBuddyProfileImage', TMessageType.CALL, self._seqid)
        args = updateBuddyProfileImage_args()
        args.requestId = requestId
        args.image = image
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddyProfileImage(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddyProfileImage_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "updateBuddyProfileImage failed: unknown result")

    def updateBuddyProfileImageAsync(self, requestId, image):
        """
        Parameters:
         - requestId
         - image
        """
        self.send_updateBuddyProfileImageAsync(requestId, image)
        return self.recv_updateBuddyProfileImageAsync()

    def send_updateBuddyProfileImageAsync(self, requestId, image):
        self._oprot.writeMessageBegin('updateBuddyProfileImageAsync', TMessageType.CALL, self._seqid)
        args = updateBuddyProfileImageAsync_args()
        args.requestId = requestId
        args.image = image
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddyProfileImageAsync(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddyProfileImageAsync_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "updateBuddyProfileImageAsync failed: unknown result")

    def updateBuddySearchId(self, requestId, searchId):
        """
        Parameters:
         - requestId
         - searchId
        """
        self.send_updateBuddySearchId(requestId, searchId)
        self.recv_updateBuddySearchId()

    def send_updateBuddySearchId(self, requestId, searchId):
        self._oprot.writeMessageBegin('updateBuddySearchId', TMessageType.CALL, self._seqid)
        args = updateBuddySearchId_args()
        args.requestId = requestId
        args.searchId = searchId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddySearchId(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddySearchId_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def updateBuddySettings(self, settings):
        """
        Parameters:
         - settings
        """
        self.send_updateBuddySettings(settings)
        self.recv_updateBuddySettings()

    def send_updateBuddySettings(self, settings):
        self._oprot.writeMessageBegin('updateBuddySettings', TMessageType.CALL, self._seqid)
        args = updateBuddySettings_args()
        args.settings = settings
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_updateBuddySettings(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = updateBuddySettings_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def uploadBuddyContent(self, contentType, content):
        """
        Parameters:
         - contentType
         - content
        """
        self.send_uploadBuddyContent(contentType, content)
        return self.recv_uploadBuddyContent()

    def send_uploadBuddyContent(self, contentType, content):
        self._oprot.writeMessageBegin('uploadBuddyContent', TMessageType.CALL, self._seqid)
        args = uploadBuddyContent_args()
        args.contentType = contentType
        args.content = content
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_uploadBuddyContent(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = uploadBuddyContent_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "uploadBuddyContent failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["addBuddyMember"] = Processor.process_addBuddyMember
        self._processMap["addBuddyMembers"] = Processor.process_addBuddyMembers
        self._processMap["blockBuddyMember"] = Processor.process_blockBuddyMember
        self._processMap["commitSendMessagesToAll"] = Processor.process_commitSendMessagesToAll
        self._processMap["commitSendMessagesToMids"] = Processor.process_commitSendMessagesToMids
        self._processMap["containsBuddyMember"] = Processor.process_containsBuddyMember
        self._processMap["downloadMessageContent"] = Processor.process_downloadMessageContent
        self._processMap["downloadMessageContentPreview"] = Processor.process_downloadMessageContentPreview
        self._processMap["downloadProfileImage"] = Processor.process_downloadProfileImage
        self._processMap["downloadProfileImagePreview"] = Processor.process_downloadProfileImagePreview
        self._processMap["getActiveMemberCountByBuddyMid"] = Processor.process_getActiveMemberCountByBuddyMid
        self._processMap["getActiveMemberMidsByBuddyMid"] = Processor.process_getActiveMemberMidsByBuddyMid
        self._processMap["getAllBuddyMembers"] = Processor.process_getAllBuddyMembers
        self._processMap["getBlockedBuddyMembers"] = Processor.process_getBlockedBuddyMembers
        self._processMap["getBlockerCountByBuddyMid"] = Processor.process_getBlockerCountByBuddyMid
        self._processMap["getBuddyDetailByMid"] = Processor.process_getBuddyDetailByMid
        self._processMap["getBuddyProfile"] = Processor.process_getBuddyProfile
        self._processMap["getContactTicket"] = Processor.process_getContactTicket
        self._processMap["getMemberCountByBuddyMid"] = Processor.process_getMemberCountByBuddyMid
        self._processMap["getSendBuddyMessageResult"] = Processor.process_getSendBuddyMessageResult
        self._processMap["getSetBuddyOnAirResult"] = Processor.process_getSetBuddyOnAirResult
        self._processMap["getUpdateBuddyProfileResult"] = Processor.process_getUpdateBuddyProfileResult
        self._processMap["isBuddyOnAirByMid"] = Processor.process_isBuddyOnAirByMid
        self._processMap["linkAndSendBuddyContentMessageToAllAsync"] = Processor.process_linkAndSendBuddyContentMessageToAllAsync
        self._processMap["linkAndSendBuddyContentMessageToMids"] = Processor.process_linkAndSendBuddyContentMessageToMids
        self._processMap["notifyBuddyBlocked"] = Processor.process_notifyBuddyBlocked
        self._processMap["notifyBuddyUnblocked"] = Processor.process_notifyBuddyUnblocked
        self._processMap["registerBuddy"] = Processor.process_registerBuddy
        self._processMap["registerBuddyAdmin"] = Processor.process_registerBuddyAdmin
        self._processMap["reissueContactTicket"] = Processor.process_reissueContactTicket
        self._processMap["removeBuddyMember"] = Processor.process_removeBuddyMember
        self._processMap["removeBuddyMembers"] = Processor.process_removeBuddyMembers
        self._processMap["sendBuddyContentMessageToAll"] = Processor.process_sendBuddyContentMessageToAll
        self._processMap["sendBuddyContentMessageToAllAsync"] = Processor.process_sendBuddyContentMessageToAllAsync
        self._processMap["sendBuddyContentMessageToMids"] = Processor.process_sendBuddyContentMessageToMids
        self._processMap["sendBuddyContentMessageToMidsAsync"] = Processor.process_sendBuddyContentMessageToMidsAsync
        self._processMap["sendBuddyMessageToAll"] = Processor.process_sendBuddyMessageToAll
        self._processMap["sendBuddyMessageToAllAsync"] = Processor.process_sendBuddyMessageToAllAsync
        self._processMap["sendBuddyMessageToMids"] = Processor.process_sendBuddyMessageToMids
        self._processMap["sendBuddyMessageToMidsAsync"] = Processor.process_sendBuddyMessageToMidsAsync
        self._processMap["sendIndividualEventToAllAsync"] = Processor.process_sendIndividualEventToAllAsync
        self._processMap["setBuddyOnAir"] = Processor.process_setBuddyOnAir
        self._processMap["setBuddyOnAirAsync"] = Processor.process_setBuddyOnAirAsync
        self._processMap["storeMessage"] = Processor.process_storeMessage
        self._processMap["unblockBuddyMember"] = Processor.process_unblockBuddyMember
        self._processMap["unregisterBuddy"] = Processor.process_unregisterBuddy
        self._processMap["unregisterBuddyAdmin"] = Processor.process_unregisterBuddyAdmin
        self._processMap["updateBuddyAdminProfileAttribute"] = Processor.process_updateBuddyAdminProfileAttribute
        self._processMap["updateBuddyAdminProfileImage"] = Processor.process_updateBuddyAdminProfileImage
        self._processMap["updateBuddyProfileAttributes"] = Processor.process_updateBuddyProfileAttributes
        self._processMap["updateBuddyProfileAttributesAsync"] = Processor.process_updateBuddyProfileAttributesAsync
        self._processMap["updateBuddyProfileImage"] = Processor.process_updateBuddyProfileImage
        self._processMap["updateBuddyProfileImageAsync"] = Processor.process_updateBuddyProfileImageAsync
        self._processMap["updateBuddySearchId"] = Processor.process_updateBuddySearchId
        self._processMap["updateBuddySettings"] = Processor.process_updateBuddySettings
        self._processMap["uploadBuddyContent"] = Processor.process_uploadBuddyContent

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

    def process_addBuddyMember(self, seqid, iprot, oprot):
        args = addBuddyMember_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addBuddyMember_result()
        try:
            self._handler.addBuddyMember(args.requestId, args.userMid)
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
        oprot.writeMessageBegin("addBuddyMember", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_addBuddyMembers(self, seqid, iprot, oprot):
        args = addBuddyMembers_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addBuddyMembers_result()
        try:
            self._handler.addBuddyMembers(args.requestId, args.userMids)
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
        oprot.writeMessageBegin("addBuddyMembers", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_blockBuddyMember(self, seqid, iprot, oprot):
        args = blockBuddyMember_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = blockBuddyMember_result()
        try:
            self._handler.blockBuddyMember(args.requestId, args.mid)
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
        oprot.writeMessageBegin("blockBuddyMember", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_commitSendMessagesToAll(self, seqid, iprot, oprot):
        args = commitSendMessagesToAll_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = commitSendMessagesToAll_result()
        try:
            result.success = self._handler.commitSendMessagesToAll(args.requestIdList)
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
        oprot.writeMessageBegin("commitSendMessagesToAll", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_commitSendMessagesToMids(self, seqid, iprot, oprot):
        args = commitSendMessagesToMids_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = commitSendMessagesToMids_result()
        try:
            result.success = self._handler.commitSendMessagesToMids(args.requestIdList, args.mids)
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
        oprot.writeMessageBegin("commitSendMessagesToMids", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_containsBuddyMember(self, seqid, iprot, oprot):
        args = containsBuddyMember_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = containsBuddyMember_result()
        try:
            result.success = self._handler.containsBuddyMember(args.requestId, args.userMid)
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
        oprot.writeMessageBegin("containsBuddyMember", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_downloadMessageContent(self, seqid, iprot, oprot):
        args = downloadMessageContent_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = downloadMessageContent_result()
        try:
            result.success = self._handler.downloadMessageContent(args.requestId, args.messageId)
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
        oprot.writeMessageBegin("downloadMessageContent", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_downloadMessageContentPreview(self, seqid, iprot, oprot):
        args = downloadMessageContentPreview_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = downloadMessageContentPreview_result()
        try:
            result.success = self._handler.downloadMessageContentPreview(args.requestId, args.messageId)
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
        oprot.writeMessageBegin("downloadMessageContentPreview", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_downloadProfileImage(self, seqid, iprot, oprot):
        args = downloadProfileImage_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = downloadProfileImage_result()
        try:
            result.success = self._handler.downloadProfileImage(args.requestId)
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
        oprot.writeMessageBegin("downloadProfileImage", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_downloadProfileImagePreview(self, seqid, iprot, oprot):
        args = downloadProfileImagePreview_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = downloadProfileImagePreview_result()
        try:
            result.success = self._handler.downloadProfileImagePreview(args.requestId)
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
        oprot.writeMessageBegin("downloadProfileImagePreview", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getActiveMemberCountByBuddyMid(self, seqid, iprot, oprot):
        args = getActiveMemberCountByBuddyMid_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getActiveMemberCountByBuddyMid_result()
        try:
            result.success = self._handler.getActiveMemberCountByBuddyMid(args.buddyMid)
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
        oprot.writeMessageBegin("getActiveMemberCountByBuddyMid", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getActiveMemberMidsByBuddyMid(self, seqid, iprot, oprot):
        args = getActiveMemberMidsByBuddyMid_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getActiveMemberMidsByBuddyMid_result()
        try:
            result.success = self._handler.getActiveMemberMidsByBuddyMid(args.buddyMid)
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
        oprot.writeMessageBegin("getActiveMemberMidsByBuddyMid", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getAllBuddyMembers(self, seqid, iprot, oprot):
        args = getAllBuddyMembers_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAllBuddyMembers_result()
        try:
            result.success = self._handler.getAllBuddyMembers()
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
        oprot.writeMessageBegin("getAllBuddyMembers", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBlockedBuddyMembers(self, seqid, iprot, oprot):
        args = getBlockedBuddyMembers_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBlockedBuddyMembers_result()
        try:
            result.success = self._handler.getBlockedBuddyMembers()
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
        oprot.writeMessageBegin("getBlockedBuddyMembers", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBlockerCountByBuddyMid(self, seqid, iprot, oprot):
        args = getBlockerCountByBuddyMid_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBlockerCountByBuddyMid_result()
        try:
            result.success = self._handler.getBlockerCountByBuddyMid(args.buddyMid)
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
        oprot.writeMessageBegin("getBlockerCountByBuddyMid", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBuddyDetailByMid(self, seqid, iprot, oprot):
        args = getBuddyDetailByMid_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBuddyDetailByMid_result()
        try:
            result.success = self._handler.getBuddyDetailByMid(args.buddyMid)
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
        oprot.writeMessageBegin("getBuddyDetailByMid", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBuddyProfile(self, seqid, iprot, oprot):
        args = getBuddyProfile_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBuddyProfile_result()
        try:
            result.success = self._handler.getBuddyProfile()
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
        oprot.writeMessageBegin("getBuddyProfile", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getContactTicket(self, seqid, iprot, oprot):
        args = getContactTicket_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getContactTicket_result()
        try:
            result.success = self._handler.getContactTicket()
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
        oprot.writeMessageBegin("getContactTicket", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getMemberCountByBuddyMid(self, seqid, iprot, oprot):
        args = getMemberCountByBuddyMid_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getMemberCountByBuddyMid_result()
        try:
            result.success = self._handler.getMemberCountByBuddyMid(args.buddyMid)
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
        oprot.writeMessageBegin("getMemberCountByBuddyMid", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getSendBuddyMessageResult(self, seqid, iprot, oprot):
        args = getSendBuddyMessageResult_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getSendBuddyMessageResult_result()
        try:
            result.success = self._handler.getSendBuddyMessageResult(args.sendBuddyMessageRequestId)
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
        oprot.writeMessageBegin("getSendBuddyMessageResult", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getSetBuddyOnAirResult(self, seqid, iprot, oprot):
        args = getSetBuddyOnAirResult_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getSetBuddyOnAirResult_result()
        try:
            result.success = self._handler.getSetBuddyOnAirResult(args.setBuddyOnAirRequestId)
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
        oprot.writeMessageBegin("getSetBuddyOnAirResult", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getUpdateBuddyProfileResult(self, seqid, iprot, oprot):
        args = getUpdateBuddyProfileResult_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getUpdateBuddyProfileResult_result()
        try:
            result.success = self._handler.getUpdateBuddyProfileResult(args.updateBuddyProfileRequestId)
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
        oprot.writeMessageBegin("getUpdateBuddyProfileResult", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_isBuddyOnAirByMid(self, seqid, iprot, oprot):
        args = isBuddyOnAirByMid_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = isBuddyOnAirByMid_result()
        try:
            result.success = self._handler.isBuddyOnAirByMid(args.buddyMid)
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
        oprot.writeMessageBegin("isBuddyOnAirByMid", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_linkAndSendBuddyContentMessageToAllAsync(self, seqid, iprot, oprot):
        args = linkAndSendBuddyContentMessageToAllAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = linkAndSendBuddyContentMessageToAllAsync_result()
        try:
            result.success = self._handler.linkAndSendBuddyContentMessageToAllAsync(args.requestId, args.msg, args.sourceContentId)
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
        oprot.writeMessageBegin("linkAndSendBuddyContentMessageToAllAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_linkAndSendBuddyContentMessageToMids(self, seqid, iprot, oprot):
        args = linkAndSendBuddyContentMessageToMids_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = linkAndSendBuddyContentMessageToMids_result()
        try:
            result.success = self._handler.linkAndSendBuddyContentMessageToMids(args.requestId, args.msg, args.sourceContentId, args.mids)
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
        oprot.writeMessageBegin("linkAndSendBuddyContentMessageToMids", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_notifyBuddyBlocked(self, seqid, iprot, oprot):
        args = notifyBuddyBlocked_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyBuddyBlocked_result()
        try:
            self._handler.notifyBuddyBlocked(args.buddyMid, args.blockerMid)
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
        oprot.writeMessageBegin("notifyBuddyBlocked", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_notifyBuddyUnblocked(self, seqid, iprot, oprot):
        args = notifyBuddyUnblocked_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = notifyBuddyUnblocked_result()
        try:
            self._handler.notifyBuddyUnblocked(args.buddyMid, args.blockerMid)
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
        oprot.writeMessageBegin("notifyBuddyUnblocked", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_registerBuddy(self, seqid, iprot, oprot):
        args = registerBuddy_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = registerBuddy_result()
        try:
            result.success = self._handler.registerBuddy(args.buddyId, args.searchId, args.displayName, args.statusMeessage, args.picture, args.settings)
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
        oprot.writeMessageBegin("registerBuddy", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_registerBuddyAdmin(self, seqid, iprot, oprot):
        args = registerBuddyAdmin_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = registerBuddyAdmin_result()
        try:
            result.success = self._handler.registerBuddyAdmin(args.buddyId, args.searchId, args.displayName, args.statusMessage, args.picture)
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
        oprot.writeMessageBegin("registerBuddyAdmin", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_reissueContactTicket(self, seqid, iprot, oprot):
        args = reissueContactTicket_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = reissueContactTicket_result()
        try:
            result.success = self._handler.reissueContactTicket(args.expirationTime, args.maxUseCount)
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
        oprot.writeMessageBegin("reissueContactTicket", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_removeBuddyMember(self, seqid, iprot, oprot):
        args = removeBuddyMember_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeBuddyMember_result()
        try:
            self._handler.removeBuddyMember(args.requestId, args.userMid)
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
        oprot.writeMessageBegin("removeBuddyMember", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_removeBuddyMembers(self, seqid, iprot, oprot):
        args = removeBuddyMembers_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeBuddyMembers_result()
        try:
            self._handler.removeBuddyMembers(args.requestId, args.userMids)
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
        oprot.writeMessageBegin("removeBuddyMembers", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyContentMessageToAll(self, seqid, iprot, oprot):
        args = sendBuddyContentMessageToAll_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyContentMessageToAll_result()
        try:
            result.success = self._handler.sendBuddyContentMessageToAll(args.requestId, args.msg, args.content)
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
        oprot.writeMessageBegin("sendBuddyContentMessageToAll", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyContentMessageToAllAsync(self, seqid, iprot, oprot):
        args = sendBuddyContentMessageToAllAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyContentMessageToAllAsync_result()
        try:
            result.success = self._handler.sendBuddyContentMessageToAllAsync(args.requestId, args.msg, args.content)
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
        oprot.writeMessageBegin("sendBuddyContentMessageToAllAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyContentMessageToMids(self, seqid, iprot, oprot):
        args = sendBuddyContentMessageToMids_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyContentMessageToMids_result()
        try:
            result.success = self._handler.sendBuddyContentMessageToMids(args.requestId, args.msg, args.content, args.mids)
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
        oprot.writeMessageBegin("sendBuddyContentMessageToMids", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyContentMessageToMidsAsync(self, seqid, iprot, oprot):
        args = sendBuddyContentMessageToMidsAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyContentMessageToMidsAsync_result()
        try:
            result.success = self._handler.sendBuddyContentMessageToMidsAsync(args.requestId, args.msg, args.content, args.mids)
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
        oprot.writeMessageBegin("sendBuddyContentMessageToMidsAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyMessageToAll(self, seqid, iprot, oprot):
        args = sendBuddyMessageToAll_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyMessageToAll_result()
        try:
            result.success = self._handler.sendBuddyMessageToAll(args.requestId, args.msg)
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
        oprot.writeMessageBegin("sendBuddyMessageToAll", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyMessageToAllAsync(self, seqid, iprot, oprot):
        args = sendBuddyMessageToAllAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyMessageToAllAsync_result()
        try:
            result.success = self._handler.sendBuddyMessageToAllAsync(args.requestId, args.msg)
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
        oprot.writeMessageBegin("sendBuddyMessageToAllAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyMessageToMids(self, seqid, iprot, oprot):
        args = sendBuddyMessageToMids_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyMessageToMids_result()
        try:
            result.success = self._handler.sendBuddyMessageToMids(args.requestId, args.msg, args.mids)
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
        oprot.writeMessageBegin("sendBuddyMessageToMids", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendBuddyMessageToMidsAsync(self, seqid, iprot, oprot):
        args = sendBuddyMessageToMidsAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendBuddyMessageToMidsAsync_result()
        try:
            result.success = self._handler.sendBuddyMessageToMidsAsync(args.requestId, args.msg, args.mids)
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
        oprot.writeMessageBegin("sendBuddyMessageToMidsAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_sendIndividualEventToAllAsync(self, seqid, iprot, oprot):
        args = sendIndividualEventToAllAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = sendIndividualEventToAllAsync_result()
        try:
            self._handler.sendIndividualEventToAllAsync(args.requestId, args.buddyMid, args.notificationStatus)
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
        oprot.writeMessageBegin("sendIndividualEventToAllAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_setBuddyOnAir(self, seqid, iprot, oprot):
        args = setBuddyOnAir_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setBuddyOnAir_result()
        try:
            result.success = self._handler.setBuddyOnAir(args.requestId, args.onAir)
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
        oprot.writeMessageBegin("setBuddyOnAir", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_setBuddyOnAirAsync(self, seqid, iprot, oprot):
        args = setBuddyOnAirAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setBuddyOnAirAsync_result()
        try:
            result.success = self._handler.setBuddyOnAirAsync(args.requestId, args.onAir)
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
        oprot.writeMessageBegin("setBuddyOnAirAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_storeMessage(self, seqid, iprot, oprot):
        args = storeMessage_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = storeMessage_result()
        try:
            result.success = self._handler.storeMessage(args.requestId, args.messageRequest)
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
        oprot.writeMessageBegin("storeMessage", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_unblockBuddyMember(self, seqid, iprot, oprot):
        args = unblockBuddyMember_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = unblockBuddyMember_result()
        try:
            self._handler.unblockBuddyMember(args.requestId, args.mid)
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
        oprot.writeMessageBegin("unblockBuddyMember", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_unregisterBuddy(self, seqid, iprot, oprot):
        args = unregisterBuddy_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = unregisterBuddy_result()
        try:
            self._handler.unregisterBuddy(args.requestId)
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
        oprot.writeMessageBegin("unregisterBuddy", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_unregisterBuddyAdmin(self, seqid, iprot, oprot):
        args = unregisterBuddyAdmin_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = unregisterBuddyAdmin_result()
        try:
            self._handler.unregisterBuddyAdmin(args.requestId)
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
        oprot.writeMessageBegin("unregisterBuddyAdmin", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddyAdminProfileAttribute(self, seqid, iprot, oprot):
        args = updateBuddyAdminProfileAttribute_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddyAdminProfileAttribute_result()
        try:
            self._handler.updateBuddyAdminProfileAttribute(args.requestId, args.attributes)
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
        oprot.writeMessageBegin("updateBuddyAdminProfileAttribute", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddyAdminProfileImage(self, seqid, iprot, oprot):
        args = updateBuddyAdminProfileImage_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddyAdminProfileImage_result()
        try:
            self._handler.updateBuddyAdminProfileImage(args.requestId, args.picture)
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
        oprot.writeMessageBegin("updateBuddyAdminProfileImage", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddyProfileAttributes(self, seqid, iprot, oprot):
        args = updateBuddyProfileAttributes_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddyProfileAttributes_result()
        try:
            result.success = self._handler.updateBuddyProfileAttributes(args.requestId, args.attributes)
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
        oprot.writeMessageBegin("updateBuddyProfileAttributes", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddyProfileAttributesAsync(self, seqid, iprot, oprot):
        args = updateBuddyProfileAttributesAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddyProfileAttributesAsync_result()
        try:
            result.success = self._handler.updateBuddyProfileAttributesAsync(args.requestId, args.attributes)
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
        oprot.writeMessageBegin("updateBuddyProfileAttributesAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddyProfileImage(self, seqid, iprot, oprot):
        args = updateBuddyProfileImage_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddyProfileImage_result()
        try:
            result.success = self._handler.updateBuddyProfileImage(args.requestId, args.image)
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
        oprot.writeMessageBegin("updateBuddyProfileImage", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddyProfileImageAsync(self, seqid, iprot, oprot):
        args = updateBuddyProfileImageAsync_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddyProfileImageAsync_result()
        try:
            result.success = self._handler.updateBuddyProfileImageAsync(args.requestId, args.image)
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
        oprot.writeMessageBegin("updateBuddyProfileImageAsync", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddySearchId(self, seqid, iprot, oprot):
        args = updateBuddySearchId_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddySearchId_result()
        try:
            self._handler.updateBuddySearchId(args.requestId, args.searchId)
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
        oprot.writeMessageBegin("updateBuddySearchId", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_updateBuddySettings(self, seqid, iprot, oprot):
        args = updateBuddySettings_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = updateBuddySettings_result()
        try:
            self._handler.updateBuddySettings(args.settings)
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
        oprot.writeMessageBegin("updateBuddySettings", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_uploadBuddyContent(self, seqid, iprot, oprot):
        args = uploadBuddyContent_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = uploadBuddyContent_result()
        try:
            result.success = self._handler.uploadBuddyContent(args.contentType, args.content)
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
        oprot.writeMessageBegin("uploadBuddyContent", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class addBuddyMember_args(object):
    """
    Attributes:
     - requestId
     - userMid
    """


    def __init__(self, requestId=None, userMid=None,):
        self.requestId = requestId
        self.userMid = userMid

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.userMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('addBuddyMember_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.userMid is not None:
            oprot.writeFieldBegin('userMid', TType.STRING, 2)
            oprot.writeString(self.userMid.encode('utf-8') if sys.version_info[0] == 2 else self.userMid)
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
all_structs.append(addBuddyMember_args)
addBuddyMember_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'userMid', 'UTF8', None, ),  # 2
)


class addBuddyMember_result(object):
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
        oprot.writeStructBegin('addBuddyMember_result')
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
all_structs.append(addBuddyMember_result)
addBuddyMember_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class addBuddyMembers_args(object):
    """
    Attributes:
     - requestId
     - userMids
    """


    def __init__(self, requestId=None, userMids=None,):
        self.requestId = requestId
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
                if ftype == TType.STRING:
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.userMids = []
                    (_etype973, _size970) = iprot.readListBegin()
                    for _i974 in range(_size970):
                        _elem975 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.userMids.append(_elem975)
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
        oprot.writeStructBegin('addBuddyMembers_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.userMids is not None:
            oprot.writeFieldBegin('userMids', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.userMids))
            for iter976 in self.userMids:
                oprot.writeString(iter976.encode('utf-8') if sys.version_info[0] == 2 else iter976)
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
all_structs.append(addBuddyMembers_args)
addBuddyMembers_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'userMids', (TType.STRING, 'UTF8', False), None, ),  # 2
)


class addBuddyMembers_result(object):
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
        oprot.writeStructBegin('addBuddyMembers_result')
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
all_structs.append(addBuddyMembers_result)
addBuddyMembers_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class blockBuddyMember_args(object):
    """
    Attributes:
     - requestId
     - mid
    """


    def __init__(self, requestId=None, mid=None,):
        self.requestId = requestId
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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
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
        oprot.writeStructBegin('blockBuddyMember_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
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
all_structs.append(blockBuddyMember_args)
blockBuddyMember_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'mid', 'UTF8', None, ),  # 2
)


class blockBuddyMember_result(object):
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
        oprot.writeStructBegin('blockBuddyMember_result')
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
all_structs.append(blockBuddyMember_result)
blockBuddyMember_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class commitSendMessagesToAll_args(object):
    """
    Attributes:
     - requestIdList
    """


    def __init__(self, requestIdList=None,):
        self.requestIdList = requestIdList

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
                    self.requestIdList = []
                    (_etype980, _size977) = iprot.readListBegin()
                    for _i981 in range(_size977):
                        _elem982 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.requestIdList.append(_elem982)
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
        oprot.writeStructBegin('commitSendMessagesToAll_args')
        if self.requestIdList is not None:
            oprot.writeFieldBegin('requestIdList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.requestIdList))
            for iter983 in self.requestIdList:
                oprot.writeString(iter983.encode('utf-8') if sys.version_info[0] == 2 else iter983)
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
all_structs.append(commitSendMessagesToAll_args)
commitSendMessagesToAll_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'requestIdList', (TType.STRING, 'UTF8', False), None, ),  # 1
)


class commitSendMessagesToAll_result(object):
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
                    (_etype987, _size984) = iprot.readListBegin()
                    for _i988 in range(_size984):
                        _elem989 = SendBuddyMessageResult()
                        _elem989.read(iprot)
                        self.success.append(_elem989)
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
        oprot.writeStructBegin('commitSendMessagesToAll_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter990 in self.success:
                iter990.write(oprot)
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
all_structs.append(commitSendMessagesToAll_result)
commitSendMessagesToAll_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [SendBuddyMessageResult, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class commitSendMessagesToMids_args(object):
    """
    Attributes:
     - requestIdList
     - mids
    """


    def __init__(self, requestIdList=None, mids=None,):
        self.requestIdList = requestIdList
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
                    self.requestIdList = []
                    (_etype994, _size991) = iprot.readListBegin()
                    for _i995 in range(_size991):
                        _elem996 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.requestIdList.append(_elem996)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype1000, _size997) = iprot.readListBegin()
                    for _i1001 in range(_size997):
                        _elem1002 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem1002)
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
        oprot.writeStructBegin('commitSendMessagesToMids_args')
        if self.requestIdList is not None:
            oprot.writeFieldBegin('requestIdList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.requestIdList))
            for iter1003 in self.requestIdList:
                oprot.writeString(iter1003.encode('utf-8') if sys.version_info[0] == 2 else iter1003)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter1004 in self.mids:
                oprot.writeString(iter1004.encode('utf-8') if sys.version_info[0] == 2 else iter1004)
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
all_structs.append(commitSendMessagesToMids_args)
commitSendMessagesToMids_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'requestIdList', (TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 2
)


class commitSendMessagesToMids_result(object):
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
                    (_etype1008, _size1005) = iprot.readListBegin()
                    for _i1009 in range(_size1005):
                        _elem1010 = SendBuddyMessageResult()
                        _elem1010.read(iprot)
                        self.success.append(_elem1010)
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
        oprot.writeStructBegin('commitSendMessagesToMids_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1011 in self.success:
                iter1011.write(oprot)
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
all_structs.append(commitSendMessagesToMids_result)
commitSendMessagesToMids_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [SendBuddyMessageResult, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class containsBuddyMember_args(object):
    """
    Attributes:
     - requestId
     - userMid
    """


    def __init__(self, requestId=None, userMid=None,):
        self.requestId = requestId
        self.userMid = userMid

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.userMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('containsBuddyMember_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.userMid is not None:
            oprot.writeFieldBegin('userMid', TType.STRING, 2)
            oprot.writeString(self.userMid.encode('utf-8') if sys.version_info[0] == 2 else self.userMid)
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
all_structs.append(containsBuddyMember_args)
containsBuddyMember_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'userMid', 'UTF8', None, ),  # 2
)


class containsBuddyMember_result(object):
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
        oprot.writeStructBegin('containsBuddyMember_result')
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
all_structs.append(containsBuddyMember_result)
containsBuddyMember_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class downloadMessageContent_args(object):
    """
    Attributes:
     - requestId
     - messageId
    """


    def __init__(self, requestId=None, messageId=None,):
        self.requestId = requestId
        self.messageId = messageId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.messageId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('downloadMessageContent_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.messageId is not None:
            oprot.writeFieldBegin('messageId', TType.STRING, 2)
            oprot.writeString(self.messageId.encode('utf-8') if sys.version_info[0] == 2 else self.messageId)
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
all_structs.append(downloadMessageContent_args)
downloadMessageContent_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'messageId', 'UTF8', None, ),  # 2
)


class downloadMessageContent_result(object):
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
                    self.success = iprot.readBinary()
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
        oprot.writeStructBegin('downloadMessageContent_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeBinary(self.success)
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
all_structs.append(downloadMessageContent_result)
downloadMessageContent_result.thrift_spec = (
    (0, TType.STRING, 'success', 'BINARY', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class downloadMessageContentPreview_args(object):
    """
    Attributes:
     - requestId
     - messageId
    """


    def __init__(self, requestId=None, messageId=None,):
        self.requestId = requestId
        self.messageId = messageId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.messageId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('downloadMessageContentPreview_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.messageId is not None:
            oprot.writeFieldBegin('messageId', TType.STRING, 2)
            oprot.writeString(self.messageId.encode('utf-8') if sys.version_info[0] == 2 else self.messageId)
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
all_structs.append(downloadMessageContentPreview_args)
downloadMessageContentPreview_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'messageId', 'UTF8', None, ),  # 2
)


class downloadMessageContentPreview_result(object):
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
                    self.success = iprot.readBinary()
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
        oprot.writeStructBegin('downloadMessageContentPreview_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeBinary(self.success)
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
all_structs.append(downloadMessageContentPreview_result)
downloadMessageContentPreview_result.thrift_spec = (
    (0, TType.STRING, 'success', 'BINARY', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class downloadProfileImage_args(object):
    """
    Attributes:
     - requestId
    """


    def __init__(self, requestId=None,):
        self.requestId = requestId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('downloadProfileImage_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
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
all_structs.append(downloadProfileImage_args)
downloadProfileImage_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
)


class downloadProfileImage_result(object):
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
                    self.success = iprot.readBinary()
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
        oprot.writeStructBegin('downloadProfileImage_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeBinary(self.success)
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
all_structs.append(downloadProfileImage_result)
downloadProfileImage_result.thrift_spec = (
    (0, TType.STRING, 'success', 'BINARY', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class downloadProfileImagePreview_args(object):
    """
    Attributes:
     - requestId
    """


    def __init__(self, requestId=None,):
        self.requestId = requestId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('downloadProfileImagePreview_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
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
all_structs.append(downloadProfileImagePreview_args)
downloadProfileImagePreview_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
)


class downloadProfileImagePreview_result(object):
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
                    self.success = iprot.readBinary()
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
        oprot.writeStructBegin('downloadProfileImagePreview_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeBinary(self.success)
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
all_structs.append(downloadProfileImagePreview_result)
downloadProfileImagePreview_result.thrift_spec = (
    (0, TType.STRING, 'success', 'BINARY', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getActiveMemberCountByBuddyMid_args(object):
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
            if fid == 2:
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
        oprot.writeStructBegin('getActiveMemberCountByBuddyMid_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
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
all_structs.append(getActiveMemberCountByBuddyMid_args)
getActiveMemberCountByBuddyMid_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
)


class getActiveMemberCountByBuddyMid_result(object):
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
        oprot.writeStructBegin('getActiveMemberCountByBuddyMid_result')
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
all_structs.append(getActiveMemberCountByBuddyMid_result)
getActiveMemberCountByBuddyMid_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getActiveMemberMidsByBuddyMid_args(object):
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
            if fid == 2:
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
        oprot.writeStructBegin('getActiveMemberMidsByBuddyMid_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
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
all_structs.append(getActiveMemberMidsByBuddyMid_args)
getActiveMemberMidsByBuddyMid_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
)


class getActiveMemberMidsByBuddyMid_result(object):
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
                    (_etype1015, _size1012) = iprot.readListBegin()
                    for _i1016 in range(_size1012):
                        _elem1017 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem1017)
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
        oprot.writeStructBegin('getActiveMemberMidsByBuddyMid_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter1018 in self.success:
                oprot.writeString(iter1018.encode('utf-8') if sys.version_info[0] == 2 else iter1018)
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
all_structs.append(getActiveMemberMidsByBuddyMid_result)
getActiveMemberMidsByBuddyMid_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getAllBuddyMembers_args(object):


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
        oprot.writeStructBegin('getAllBuddyMembers_args')
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
all_structs.append(getAllBuddyMembers_args)
getAllBuddyMembers_args.thrift_spec = (
)


class getAllBuddyMembers_result(object):
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
                    (_etype1022, _size1019) = iprot.readListBegin()
                    for _i1023 in range(_size1019):
                        _elem1024 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem1024)
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
        oprot.writeStructBegin('getAllBuddyMembers_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter1025 in self.success:
                oprot.writeString(iter1025.encode('utf-8') if sys.version_info[0] == 2 else iter1025)
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
all_structs.append(getAllBuddyMembers_result)
getAllBuddyMembers_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBlockedBuddyMembers_args(object):


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
        oprot.writeStructBegin('getBlockedBuddyMembers_args')
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
all_structs.append(getBlockedBuddyMembers_args)
getBlockedBuddyMembers_args.thrift_spec = (
)


class getBlockedBuddyMembers_result(object):
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
                    (_etype1029, _size1026) = iprot.readListBegin()
                    for _i1030 in range(_size1026):
                        _elem1031 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem1031)
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
        oprot.writeStructBegin('getBlockedBuddyMembers_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter1032 in self.success:
                oprot.writeString(iter1032.encode('utf-8') if sys.version_info[0] == 2 else iter1032)
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
all_structs.append(getBlockedBuddyMembers_result)
getBlockedBuddyMembers_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBlockerCountByBuddyMid_args(object):
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
            if fid == 2:
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
        oprot.writeStructBegin('getBlockerCountByBuddyMid_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
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
all_structs.append(getBlockerCountByBuddyMid_args)
getBlockerCountByBuddyMid_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
)


class getBlockerCountByBuddyMid_result(object):
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
        oprot.writeStructBegin('getBlockerCountByBuddyMid_result')
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
all_structs.append(getBlockerCountByBuddyMid_result)
getBlockerCountByBuddyMid_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBuddyDetailByMid_args(object):
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
            if fid == 2:
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
        oprot.writeStructBegin('getBuddyDetailByMid_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
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
all_structs.append(getBuddyDetailByMid_args)
getBuddyDetailByMid_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
)


class getBuddyDetailByMid_result(object):
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
                    self.success = BuddyDetail()
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
        oprot.writeStructBegin('getBuddyDetailByMid_result')
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
all_structs.append(getBuddyDetailByMid_result)
getBuddyDetailByMid_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BuddyDetail, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBuddyProfile_args(object):


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
        oprot.writeStructBegin('getBuddyProfile_args')
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
all_structs.append(getBuddyProfile_args)
getBuddyProfile_args.thrift_spec = (
)


class getBuddyProfile_result(object):
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
                    self.success = BuddyProfile()
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
        oprot.writeStructBegin('getBuddyProfile_result')
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
all_structs.append(getBuddyProfile_result)
getBuddyProfile_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BuddyProfile, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getContactTicket_args(object):


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
        oprot.writeStructBegin('getContactTicket_args')
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
all_structs.append(getContactTicket_args)
getContactTicket_args.thrift_spec = (
)


class getContactTicket_result(object):
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
                    self.success = Ticket()
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
        oprot.writeStructBegin('getContactTicket_result')
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
all_structs.append(getContactTicket_result)
getContactTicket_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [Ticket, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getMemberCountByBuddyMid_args(object):
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
            if fid == 2:
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
        oprot.writeStructBegin('getMemberCountByBuddyMid_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
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
all_structs.append(getMemberCountByBuddyMid_args)
getMemberCountByBuddyMid_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
)


class getMemberCountByBuddyMid_result(object):
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
        oprot.writeStructBegin('getMemberCountByBuddyMid_result')
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
all_structs.append(getMemberCountByBuddyMid_result)
getMemberCountByBuddyMid_result.thrift_spec = (
    (0, TType.I64, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getSendBuddyMessageResult_args(object):
    """
    Attributes:
     - sendBuddyMessageRequestId
    """


    def __init__(self, sendBuddyMessageRequestId=None,):
        self.sendBuddyMessageRequestId = sendBuddyMessageRequestId

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
                    self.sendBuddyMessageRequestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getSendBuddyMessageResult_args')
        if self.sendBuddyMessageRequestId is not None:
            oprot.writeFieldBegin('sendBuddyMessageRequestId', TType.STRING, 1)
            oprot.writeString(self.sendBuddyMessageRequestId.encode('utf-8') if sys.version_info[0] == 2 else self.sendBuddyMessageRequestId)
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
all_structs.append(getSendBuddyMessageResult_args)
getSendBuddyMessageResult_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'sendBuddyMessageRequestId', 'UTF8', None, ),  # 1
)


class getSendBuddyMessageResult_result(object):
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
                    self.success = SendBuddyMessageResult()
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
        oprot.writeStructBegin('getSendBuddyMessageResult_result')
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
all_structs.append(getSendBuddyMessageResult_result)
getSendBuddyMessageResult_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SendBuddyMessageResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getSetBuddyOnAirResult_args(object):
    """
    Attributes:
     - setBuddyOnAirRequestId
    """


    def __init__(self, setBuddyOnAirRequestId=None,):
        self.setBuddyOnAirRequestId = setBuddyOnAirRequestId

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
                    self.setBuddyOnAirRequestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getSetBuddyOnAirResult_args')
        if self.setBuddyOnAirRequestId is not None:
            oprot.writeFieldBegin('setBuddyOnAirRequestId', TType.STRING, 1)
            oprot.writeString(self.setBuddyOnAirRequestId.encode('utf-8') if sys.version_info[0] == 2 else self.setBuddyOnAirRequestId)
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
all_structs.append(getSetBuddyOnAirResult_args)
getSetBuddyOnAirResult_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'setBuddyOnAirRequestId', 'UTF8', None, ),  # 1
)


class getSetBuddyOnAirResult_result(object):
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
                    self.success = SetBuddyOnAirResult()
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
        oprot.writeStructBegin('getSetBuddyOnAirResult_result')
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
all_structs.append(getSetBuddyOnAirResult_result)
getSetBuddyOnAirResult_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SetBuddyOnAirResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getUpdateBuddyProfileResult_args(object):
    """
    Attributes:
     - updateBuddyProfileRequestId
    """


    def __init__(self, updateBuddyProfileRequestId=None,):
        self.updateBuddyProfileRequestId = updateBuddyProfileRequestId

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
                    self.updateBuddyProfileRequestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getUpdateBuddyProfileResult_args')
        if self.updateBuddyProfileRequestId is not None:
            oprot.writeFieldBegin('updateBuddyProfileRequestId', TType.STRING, 1)
            oprot.writeString(self.updateBuddyProfileRequestId.encode('utf-8') if sys.version_info[0] == 2 else self.updateBuddyProfileRequestId)
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
all_structs.append(getUpdateBuddyProfileResult_args)
getUpdateBuddyProfileResult_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'updateBuddyProfileRequestId', 'UTF8', None, ),  # 1
)


class getUpdateBuddyProfileResult_result(object):
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
                    self.success = UpdateBuddyProfileResult()
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
        oprot.writeStructBegin('getUpdateBuddyProfileResult_result')
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
all_structs.append(getUpdateBuddyProfileResult_result)
getUpdateBuddyProfileResult_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [UpdateBuddyProfileResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class isBuddyOnAirByMid_args(object):
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
            if fid == 2:
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
        oprot.writeStructBegin('isBuddyOnAirByMid_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
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
all_structs.append(isBuddyOnAirByMid_args)
isBuddyOnAirByMid_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
)


class isBuddyOnAirByMid_result(object):
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
        oprot.writeStructBegin('isBuddyOnAirByMid_result')
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
all_structs.append(isBuddyOnAirByMid_result)
isBuddyOnAirByMid_result.thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class linkAndSendBuddyContentMessageToAllAsync_args(object):
    """
    Attributes:
     - requestId
     - msg
     - sourceContentId
    """


    def __init__(self, requestId=None, msg=None, sourceContentId=None,):
        self.requestId = requestId
        self.msg = msg
        self.sourceContentId = sourceContentId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.sourceContentId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('linkAndSendBuddyContentMessageToAllAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.sourceContentId is not None:
            oprot.writeFieldBegin('sourceContentId', TType.STRING, 3)
            oprot.writeString(self.sourceContentId.encode('utf-8') if sys.version_info[0] == 2 else self.sourceContentId)
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
all_structs.append(linkAndSendBuddyContentMessageToAllAsync_args)
linkAndSendBuddyContentMessageToAllAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.STRING, 'sourceContentId', 'UTF8', None, ),  # 3
)


class linkAndSendBuddyContentMessageToAllAsync_result(object):
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
        oprot.writeStructBegin('linkAndSendBuddyContentMessageToAllAsync_result')
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
all_structs.append(linkAndSendBuddyContentMessageToAllAsync_result)
linkAndSendBuddyContentMessageToAllAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class linkAndSendBuddyContentMessageToMids_args(object):
    """
    Attributes:
     - requestId
     - msg
     - sourceContentId
     - mids
    """


    def __init__(self, requestId=None, msg=None, sourceContentId=None, mids=None,):
        self.requestId = requestId
        self.msg = msg
        self.sourceContentId = sourceContentId
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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.sourceContentId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype1036, _size1033) = iprot.readListBegin()
                    for _i1037 in range(_size1033):
                        _elem1038 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem1038)
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
        oprot.writeStructBegin('linkAndSendBuddyContentMessageToMids_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.sourceContentId is not None:
            oprot.writeFieldBegin('sourceContentId', TType.STRING, 3)
            oprot.writeString(self.sourceContentId.encode('utf-8') if sys.version_info[0] == 2 else self.sourceContentId)
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter1039 in self.mids:
                oprot.writeString(iter1039.encode('utf-8') if sys.version_info[0] == 2 else iter1039)
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
all_structs.append(linkAndSendBuddyContentMessageToMids_args)
linkAndSendBuddyContentMessageToMids_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.STRING, 'sourceContentId', 'UTF8', None, ),  # 3
    (4, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 4
)


class linkAndSendBuddyContentMessageToMids_result(object):
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
                    self.success = SendBuddyMessageResult()
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
        oprot.writeStructBegin('linkAndSendBuddyContentMessageToMids_result')
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
all_structs.append(linkAndSendBuddyContentMessageToMids_result)
linkAndSendBuddyContentMessageToMids_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SendBuddyMessageResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class notifyBuddyBlocked_args(object):
    """
    Attributes:
     - buddyMid
     - blockerMid
    """


    def __init__(self, buddyMid=None, blockerMid=None,):
        self.buddyMid = buddyMid
        self.blockerMid = blockerMid

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
            elif fid == 2:
                if ftype == TType.STRING:
                    self.blockerMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('notifyBuddyBlocked_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 1)
            oprot.writeString(self.buddyMid.encode('utf-8') if sys.version_info[0] == 2 else self.buddyMid)
            oprot.writeFieldEnd()
        if self.blockerMid is not None:
            oprot.writeFieldBegin('blockerMid', TType.STRING, 2)
            oprot.writeString(self.blockerMid.encode('utf-8') if sys.version_info[0] == 2 else self.blockerMid)
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
all_structs.append(notifyBuddyBlocked_args)
notifyBuddyBlocked_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'blockerMid', 'UTF8', None, ),  # 2
)


class notifyBuddyBlocked_result(object):
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
        oprot.writeStructBegin('notifyBuddyBlocked_result')
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
all_structs.append(notifyBuddyBlocked_result)
notifyBuddyBlocked_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class notifyBuddyUnblocked_args(object):
    """
    Attributes:
     - buddyMid
     - blockerMid
    """


    def __init__(self, buddyMid=None, blockerMid=None,):
        self.buddyMid = buddyMid
        self.blockerMid = blockerMid

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
            elif fid == 2:
                if ftype == TType.STRING:
                    self.blockerMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('notifyBuddyUnblocked_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 1)
            oprot.writeString(self.buddyMid.encode('utf-8') if sys.version_info[0] == 2 else self.buddyMid)
            oprot.writeFieldEnd()
        if self.blockerMid is not None:
            oprot.writeFieldBegin('blockerMid', TType.STRING, 2)
            oprot.writeString(self.blockerMid.encode('utf-8') if sys.version_info[0] == 2 else self.blockerMid)
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
all_structs.append(notifyBuddyUnblocked_args)
notifyBuddyUnblocked_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'blockerMid', 'UTF8', None, ),  # 2
)


class notifyBuddyUnblocked_result(object):
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
        oprot.writeStructBegin('notifyBuddyUnblocked_result')
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
all_structs.append(notifyBuddyUnblocked_result)
notifyBuddyUnblocked_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class registerBuddy_args(object):
    """
    Attributes:
     - buddyId
     - searchId
     - displayName
     - statusMeessage
     - picture
     - settings
    """


    def __init__(self, buddyId=None, searchId=None, displayName=None, statusMeessage=None, picture=None, settings=None,):
        self.buddyId = buddyId
        self.searchId = searchId
        self.displayName = displayName
        self.statusMeessage = statusMeessage
        self.picture = picture
        self.settings = settings

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
                    self.buddyId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.searchId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.statusMeessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.picture = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.MAP:
                    self.settings = {}
                    (_ktype1041, _vtype1042, _size1040) = iprot.readMapBegin()
                    for _i1044 in range(_size1040):
                        _key1045 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val1046 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.settings[_key1045] = _val1046
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('registerBuddy_args')
        if self.buddyId is not None:
            oprot.writeFieldBegin('buddyId', TType.STRING, 2)
            oprot.writeString(self.buddyId.encode('utf-8') if sys.version_info[0] == 2 else self.buddyId)
            oprot.writeFieldEnd()
        if self.searchId is not None:
            oprot.writeFieldBegin('searchId', TType.STRING, 3)
            oprot.writeString(self.searchId.encode('utf-8') if sys.version_info[0] == 2 else self.searchId)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 4)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.statusMeessage is not None:
            oprot.writeFieldBegin('statusMeessage', TType.STRING, 5)
            oprot.writeString(self.statusMeessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMeessage)
            oprot.writeFieldEnd()
        if self.picture is not None:
            oprot.writeFieldBegin('picture', TType.STRING, 6)
            oprot.writeBinary(self.picture)
            oprot.writeFieldEnd()
        if self.settings is not None:
            oprot.writeFieldBegin('settings', TType.MAP, 7)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.settings))
            for kiter1047, viter1048 in self.settings.items():
                oprot.writeString(kiter1047.encode('utf-8') if sys.version_info[0] == 2 else kiter1047)
                oprot.writeString(viter1048.encode('utf-8') if sys.version_info[0] == 2 else viter1048)
            oprot.writeMapEnd()
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
all_structs.append(registerBuddy_args)
registerBuddy_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyId', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'searchId', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'displayName', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'statusMeessage', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'picture', 'BINARY', None, ),  # 6
    (7, TType.MAP, 'settings', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 7
)


class registerBuddy_result(object):
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
        oprot.writeStructBegin('registerBuddy_result')
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
all_structs.append(registerBuddy_result)
registerBuddy_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class registerBuddyAdmin_args(object):
    """
    Attributes:
     - buddyId
     - searchId
     - displayName
     - statusMessage
     - picture
    """


    def __init__(self, buddyId=None, searchId=None, displayName=None, statusMessage=None, picture=None,):
        self.buddyId = buddyId
        self.searchId = searchId
        self.displayName = displayName
        self.statusMessage = statusMessage
        self.picture = picture

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
                    self.buddyId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.searchId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.statusMessage = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.picture = iprot.readBinary()
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
        oprot.writeStructBegin('registerBuddyAdmin_args')
        if self.buddyId is not None:
            oprot.writeFieldBegin('buddyId', TType.STRING, 2)
            oprot.writeString(self.buddyId.encode('utf-8') if sys.version_info[0] == 2 else self.buddyId)
            oprot.writeFieldEnd()
        if self.searchId is not None:
            oprot.writeFieldBegin('searchId', TType.STRING, 3)
            oprot.writeString(self.searchId.encode('utf-8') if sys.version_info[0] == 2 else self.searchId)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 4)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.statusMessage is not None:
            oprot.writeFieldBegin('statusMessage', TType.STRING, 5)
            oprot.writeString(self.statusMessage.encode('utf-8') if sys.version_info[0] == 2 else self.statusMessage)
            oprot.writeFieldEnd()
        if self.picture is not None:
            oprot.writeFieldBegin('picture', TType.STRING, 6)
            oprot.writeBinary(self.picture)
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
all_structs.append(registerBuddyAdmin_args)
registerBuddyAdmin_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'buddyId', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'searchId', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'displayName', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'statusMessage', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'picture', 'BINARY', None, ),  # 6
)


class registerBuddyAdmin_result(object):
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
        oprot.writeStructBegin('registerBuddyAdmin_result')
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
all_structs.append(registerBuddyAdmin_result)
registerBuddyAdmin_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class reissueContactTicket_args(object):
    """
    Attributes:
     - expirationTime
     - maxUseCount
    """


    def __init__(self, expirationTime=None, maxUseCount=None,):
        self.expirationTime = expirationTime
        self.maxUseCount = maxUseCount

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 3:
                if ftype == TType.I64:
                    self.expirationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.maxUseCount = iprot.readI32()
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
        oprot.writeStructBegin('reissueContactTicket_args')
        if self.expirationTime is not None:
            oprot.writeFieldBegin('expirationTime', TType.I64, 3)
            oprot.writeI64(self.expirationTime)
            oprot.writeFieldEnd()
        if self.maxUseCount is not None:
            oprot.writeFieldBegin('maxUseCount', TType.I32, 4)
            oprot.writeI32(self.maxUseCount)
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
all_structs.append(reissueContactTicket_args)
reissueContactTicket_args.thrift_spec = (
    None,  # 0
    None,  # 1
    None,  # 2
    (3, TType.I64, 'expirationTime', None, None, ),  # 3
    (4, TType.I32, 'maxUseCount', None, None, ),  # 4
)


class reissueContactTicket_result(object):
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
        oprot.writeStructBegin('reissueContactTicket_result')
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
all_structs.append(reissueContactTicket_result)
reissueContactTicket_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class removeBuddyMember_args(object):
    """
    Attributes:
     - requestId
     - userMid
    """


    def __init__(self, requestId=None, userMid=None,):
        self.requestId = requestId
        self.userMid = userMid

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.userMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('removeBuddyMember_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.userMid is not None:
            oprot.writeFieldBegin('userMid', TType.STRING, 2)
            oprot.writeString(self.userMid.encode('utf-8') if sys.version_info[0] == 2 else self.userMid)
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
all_structs.append(removeBuddyMember_args)
removeBuddyMember_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'userMid', 'UTF8', None, ),  # 2
)


class removeBuddyMember_result(object):
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
        oprot.writeStructBegin('removeBuddyMember_result')
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
all_structs.append(removeBuddyMember_result)
removeBuddyMember_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class removeBuddyMembers_args(object):
    """
    Attributes:
     - requestId
     - userMids
    """


    def __init__(self, requestId=None, userMids=None,):
        self.requestId = requestId
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
                if ftype == TType.STRING:
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.userMids = []
                    (_etype1052, _size1049) = iprot.readListBegin()
                    for _i1053 in range(_size1049):
                        _elem1054 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.userMids.append(_elem1054)
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
        oprot.writeStructBegin('removeBuddyMembers_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.userMids is not None:
            oprot.writeFieldBegin('userMids', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.userMids))
            for iter1055 in self.userMids:
                oprot.writeString(iter1055.encode('utf-8') if sys.version_info[0] == 2 else iter1055)
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
all_structs.append(removeBuddyMembers_args)
removeBuddyMembers_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'userMids', (TType.STRING, 'UTF8', False), None, ),  # 2
)


class removeBuddyMembers_result(object):
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
        oprot.writeStructBegin('removeBuddyMembers_result')
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
all_structs.append(removeBuddyMembers_result)
removeBuddyMembers_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyContentMessageToAll_args(object):
    """
    Attributes:
     - requestId
     - msg
     - content
    """


    def __init__(self, requestId=None, msg=None, content=None,):
        self.requestId = requestId
        self.msg = msg
        self.content = content

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.content = iprot.readBinary()
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
        oprot.writeStructBegin('sendBuddyContentMessageToAll_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.STRING, 3)
            oprot.writeBinary(self.content)
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
all_structs.append(sendBuddyContentMessageToAll_args)
sendBuddyContentMessageToAll_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.STRING, 'content', 'BINARY', None, ),  # 3
)


class sendBuddyContentMessageToAll_result(object):
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
                    self.success = SendBuddyMessageResult()
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
        oprot.writeStructBegin('sendBuddyContentMessageToAll_result')
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
all_structs.append(sendBuddyContentMessageToAll_result)
sendBuddyContentMessageToAll_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SendBuddyMessageResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyContentMessageToAllAsync_args(object):
    """
    Attributes:
     - requestId
     - msg
     - content
    """


    def __init__(self, requestId=None, msg=None, content=None,):
        self.requestId = requestId
        self.msg = msg
        self.content = content

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.content = iprot.readBinary()
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
        oprot.writeStructBegin('sendBuddyContentMessageToAllAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.STRING, 3)
            oprot.writeBinary(self.content)
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
all_structs.append(sendBuddyContentMessageToAllAsync_args)
sendBuddyContentMessageToAllAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.STRING, 'content', 'BINARY', None, ),  # 3
)


class sendBuddyContentMessageToAllAsync_result(object):
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
        oprot.writeStructBegin('sendBuddyContentMessageToAllAsync_result')
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
all_structs.append(sendBuddyContentMessageToAllAsync_result)
sendBuddyContentMessageToAllAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyContentMessageToMids_args(object):
    """
    Attributes:
     - requestId
     - msg
     - content
     - mids
    """


    def __init__(self, requestId=None, msg=None, content=None, mids=None,):
        self.requestId = requestId
        self.msg = msg
        self.content = content
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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.content = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype1059, _size1056) = iprot.readListBegin()
                    for _i1060 in range(_size1056):
                        _elem1061 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem1061)
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
        oprot.writeStructBegin('sendBuddyContentMessageToMids_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.STRING, 3)
            oprot.writeBinary(self.content)
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter1062 in self.mids:
                oprot.writeString(iter1062.encode('utf-8') if sys.version_info[0] == 2 else iter1062)
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
all_structs.append(sendBuddyContentMessageToMids_args)
sendBuddyContentMessageToMids_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.STRING, 'content', 'BINARY', None, ),  # 3
    (4, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 4
)


class sendBuddyContentMessageToMids_result(object):
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
                    self.success = SendBuddyMessageResult()
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
        oprot.writeStructBegin('sendBuddyContentMessageToMids_result')
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
all_structs.append(sendBuddyContentMessageToMids_result)
sendBuddyContentMessageToMids_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SendBuddyMessageResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyContentMessageToMidsAsync_args(object):
    """
    Attributes:
     - requestId
     - msg
     - content
     - mids
    """


    def __init__(self, requestId=None, msg=None, content=None, mids=None,):
        self.requestId = requestId
        self.msg = msg
        self.content = content
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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.content = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype1066, _size1063) = iprot.readListBegin()
                    for _i1067 in range(_size1063):
                        _elem1068 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem1068)
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
        oprot.writeStructBegin('sendBuddyContentMessageToMidsAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.STRING, 3)
            oprot.writeBinary(self.content)
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter1069 in self.mids:
                oprot.writeString(iter1069.encode('utf-8') if sys.version_info[0] == 2 else iter1069)
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
all_structs.append(sendBuddyContentMessageToMidsAsync_args)
sendBuddyContentMessageToMidsAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.STRING, 'content', 'BINARY', None, ),  # 3
    (4, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 4
)


class sendBuddyContentMessageToMidsAsync_result(object):
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
        oprot.writeStructBegin('sendBuddyContentMessageToMidsAsync_result')
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
all_structs.append(sendBuddyContentMessageToMidsAsync_result)
sendBuddyContentMessageToMidsAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyMessageToAll_args(object):
    """
    Attributes:
     - requestId
     - msg
    """


    def __init__(self, requestId=None, msg=None,):
        self.requestId = requestId
        self.msg = msg

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
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
        oprot.writeStructBegin('sendBuddyMessageToAll_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
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
all_structs.append(sendBuddyMessageToAll_args)
sendBuddyMessageToAll_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
)


class sendBuddyMessageToAll_result(object):
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
                    self.success = SendBuddyMessageResult()
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
        oprot.writeStructBegin('sendBuddyMessageToAll_result')
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
all_structs.append(sendBuddyMessageToAll_result)
sendBuddyMessageToAll_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SendBuddyMessageResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyMessageToAllAsync_args(object):
    """
    Attributes:
     - requestId
     - msg
    """


    def __init__(self, requestId=None, msg=None,):
        self.requestId = requestId
        self.msg = msg

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
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
        oprot.writeStructBegin('sendBuddyMessageToAllAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
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
all_structs.append(sendBuddyMessageToAllAsync_args)
sendBuddyMessageToAllAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
)


class sendBuddyMessageToAllAsync_result(object):
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
        oprot.writeStructBegin('sendBuddyMessageToAllAsync_result')
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
all_structs.append(sendBuddyMessageToAllAsync_result)
sendBuddyMessageToAllAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyMessageToMids_args(object):
    """
    Attributes:
     - requestId
     - msg
     - mids
    """


    def __init__(self, requestId=None, msg=None, mids=None,):
        self.requestId = requestId
        self.msg = msg
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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype1073, _size1070) = iprot.readListBegin()
                    for _i1074 in range(_size1070):
                        _elem1075 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem1075)
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
        oprot.writeStructBegin('sendBuddyMessageToMids_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter1076 in self.mids:
                oprot.writeString(iter1076.encode('utf-8') if sys.version_info[0] == 2 else iter1076)
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
all_structs.append(sendBuddyMessageToMids_args)
sendBuddyMessageToMids_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 3
)


class sendBuddyMessageToMids_result(object):
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
                    self.success = SendBuddyMessageResult()
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
        oprot.writeStructBegin('sendBuddyMessageToMids_result')
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
all_structs.append(sendBuddyMessageToMids_result)
sendBuddyMessageToMids_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SendBuddyMessageResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendBuddyMessageToMidsAsync_args(object):
    """
    Attributes:
     - requestId
     - msg
     - mids
    """


    def __init__(self, requestId=None, msg=None, mids=None,):
        self.requestId = requestId
        self.msg = msg
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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.msg = Message()
                    self.msg.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.mids = []
                    (_etype1080, _size1077) = iprot.readListBegin()
                    for _i1081 in range(_size1077):
                        _elem1082 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.mids.append(_elem1082)
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
        oprot.writeStructBegin('sendBuddyMessageToMidsAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRUCT, 2)
            self.msg.write(oprot)
            oprot.writeFieldEnd()
        if self.mids is not None:
            oprot.writeFieldBegin('mids', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.mids))
            for iter1083 in self.mids:
                oprot.writeString(iter1083.encode('utf-8') if sys.version_info[0] == 2 else iter1083)
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
all_structs.append(sendBuddyMessageToMidsAsync_args)
sendBuddyMessageToMidsAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'msg', [Message, None], None, ),  # 2
    (3, TType.LIST, 'mids', (TType.STRING, 'UTF8', False), None, ),  # 3
)


class sendBuddyMessageToMidsAsync_result(object):
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
        oprot.writeStructBegin('sendBuddyMessageToMidsAsync_result')
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
all_structs.append(sendBuddyMessageToMidsAsync_result)
sendBuddyMessageToMidsAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class sendIndividualEventToAllAsync_args(object):
    """
    Attributes:
     - requestId
     - buddyMid
     - notificationStatus
    """


    def __init__(self, requestId=None, buddyMid=None, notificationStatus=None,):
        self.requestId = requestId
        self.buddyMid = buddyMid
        self.notificationStatus = notificationStatus

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.buddyMid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.notificationStatus = iprot.readI32()
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
        oprot.writeStructBegin('sendIndividualEventToAllAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 2)
            oprot.writeString(self.buddyMid.encode('utf-8') if sys.version_info[0] == 2 else self.buddyMid)
            oprot.writeFieldEnd()
        if self.notificationStatus is not None:
            oprot.writeFieldBegin('notificationStatus', TType.I32, 3)
            oprot.writeI32(self.notificationStatus)
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
all_structs.append(sendIndividualEventToAllAsync_args)
sendIndividualEventToAllAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 2
    (3, TType.I32, 'notificationStatus', None, None, ),  # 3
)


class sendIndividualEventToAllAsync_result(object):
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
        oprot.writeStructBegin('sendIndividualEventToAllAsync_result')
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
all_structs.append(sendIndividualEventToAllAsync_result)
sendIndividualEventToAllAsync_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class setBuddyOnAir_args(object):
    """
    Attributes:
     - requestId
     - onAir
    """


    def __init__(self, requestId=None, onAir=None,):
        self.requestId = requestId
        self.onAir = onAir

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.onAir = iprot.readBool()
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
        oprot.writeStructBegin('setBuddyOnAir_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.onAir is not None:
            oprot.writeFieldBegin('onAir', TType.BOOL, 2)
            oprot.writeBool(self.onAir)
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
all_structs.append(setBuddyOnAir_args)
setBuddyOnAir_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.BOOL, 'onAir', None, None, ),  # 2
)


class setBuddyOnAir_result(object):
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
                    self.success = SetBuddyOnAirResult()
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
        oprot.writeStructBegin('setBuddyOnAir_result')
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
all_structs.append(setBuddyOnAir_result)
setBuddyOnAir_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SetBuddyOnAirResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class setBuddyOnAirAsync_args(object):
    """
    Attributes:
     - requestId
     - onAir
    """


    def __init__(self, requestId=None, onAir=None,):
        self.requestId = requestId
        self.onAir = onAir

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.onAir = iprot.readBool()
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
        oprot.writeStructBegin('setBuddyOnAirAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.onAir is not None:
            oprot.writeFieldBegin('onAir', TType.BOOL, 2)
            oprot.writeBool(self.onAir)
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
all_structs.append(setBuddyOnAirAsync_args)
setBuddyOnAirAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.BOOL, 'onAir', None, None, ),  # 2
)


class setBuddyOnAirAsync_result(object):
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
        oprot.writeStructBegin('setBuddyOnAirAsync_result')
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
all_structs.append(setBuddyOnAirAsync_result)
setBuddyOnAirAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class storeMessage_args(object):
    """
    Attributes:
     - requestId
     - messageRequest
    """


    def __init__(self, requestId=None, messageRequest=None,):
        self.requestId = requestId
        self.messageRequest = messageRequest

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.messageRequest = BuddyMessageRequest()
                    self.messageRequest.read(iprot)
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
        oprot.writeStructBegin('storeMessage_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.messageRequest is not None:
            oprot.writeFieldBegin('messageRequest', TType.STRUCT, 2)
            self.messageRequest.write(oprot)
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
all_structs.append(storeMessage_args)
storeMessage_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'messageRequest', [BuddyMessageRequest, None], None, ),  # 2
)


class storeMessage_result(object):
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
                    self.success = SendBuddyMessageResult()
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
        oprot.writeStructBegin('storeMessage_result')
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
all_structs.append(storeMessage_result)
storeMessage_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SendBuddyMessageResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class unblockBuddyMember_args(object):
    """
    Attributes:
     - requestId
     - mid
    """


    def __init__(self, requestId=None, mid=None,):
        self.requestId = requestId
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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
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
        oprot.writeStructBegin('unblockBuddyMember_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
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
all_structs.append(unblockBuddyMember_args)
unblockBuddyMember_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'mid', 'UTF8', None, ),  # 2
)


class unblockBuddyMember_result(object):
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
        oprot.writeStructBegin('unblockBuddyMember_result')
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
all_structs.append(unblockBuddyMember_result)
unblockBuddyMember_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class unregisterBuddy_args(object):
    """
    Attributes:
     - requestId
    """


    def __init__(self, requestId=None,):
        self.requestId = requestId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('unregisterBuddy_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
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
all_structs.append(unregisterBuddy_args)
unregisterBuddy_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
)


class unregisterBuddy_result(object):
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
        oprot.writeStructBegin('unregisterBuddy_result')
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
all_structs.append(unregisterBuddy_result)
unregisterBuddy_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class unregisterBuddyAdmin_args(object):
    """
    Attributes:
     - requestId
    """


    def __init__(self, requestId=None,):
        self.requestId = requestId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('unregisterBuddyAdmin_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
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
all_structs.append(unregisterBuddyAdmin_args)
unregisterBuddyAdmin_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
)


class unregisterBuddyAdmin_result(object):
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
        oprot.writeStructBegin('unregisterBuddyAdmin_result')
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
all_structs.append(unregisterBuddyAdmin_result)
unregisterBuddyAdmin_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddyAdminProfileAttribute_args(object):
    """
    Attributes:
     - requestId
     - attributes
    """


    def __init__(self, requestId=None, attributes=None,):
        self.requestId = requestId
        self.attributes = attributes

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.attributes = {}
                    (_ktype1085, _vtype1086, _size1084) = iprot.readMapBegin()
                    for _i1088 in range(_size1084):
                        _key1089 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val1090 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.attributes[_key1089] = _val1090
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('updateBuddyAdminProfileAttribute_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.attributes is not None:
            oprot.writeFieldBegin('attributes', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.attributes))
            for kiter1091, viter1092 in self.attributes.items():
                oprot.writeString(kiter1091.encode('utf-8') if sys.version_info[0] == 2 else kiter1091)
                oprot.writeString(viter1092.encode('utf-8') if sys.version_info[0] == 2 else viter1092)
            oprot.writeMapEnd()
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
all_structs.append(updateBuddyAdminProfileAttribute_args)
updateBuddyAdminProfileAttribute_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.MAP, 'attributes', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)


class updateBuddyAdminProfileAttribute_result(object):
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
        oprot.writeStructBegin('updateBuddyAdminProfileAttribute_result')
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
all_structs.append(updateBuddyAdminProfileAttribute_result)
updateBuddyAdminProfileAttribute_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddyAdminProfileImage_args(object):
    """
    Attributes:
     - requestId
     - picture
    """


    def __init__(self, requestId=None, picture=None,):
        self.requestId = requestId
        self.picture = picture

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.picture = iprot.readBinary()
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
        oprot.writeStructBegin('updateBuddyAdminProfileImage_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.picture is not None:
            oprot.writeFieldBegin('picture', TType.STRING, 2)
            oprot.writeBinary(self.picture)
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
all_structs.append(updateBuddyAdminProfileImage_args)
updateBuddyAdminProfileImage_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'picture', 'BINARY', None, ),  # 2
)


class updateBuddyAdminProfileImage_result(object):
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
        oprot.writeStructBegin('updateBuddyAdminProfileImage_result')
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
all_structs.append(updateBuddyAdminProfileImage_result)
updateBuddyAdminProfileImage_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddyProfileAttributes_args(object):
    """
    Attributes:
     - requestId
     - attributes
    """


    def __init__(self, requestId=None, attributes=None,):
        self.requestId = requestId
        self.attributes = attributes

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.attributes = {}
                    (_ktype1094, _vtype1095, _size1093) = iprot.readMapBegin()
                    for _i1097 in range(_size1093):
                        _key1098 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val1099 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.attributes[_key1098] = _val1099
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('updateBuddyProfileAttributes_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.attributes is not None:
            oprot.writeFieldBegin('attributes', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.attributes))
            for kiter1100, viter1101 in self.attributes.items():
                oprot.writeString(kiter1100.encode('utf-8') if sys.version_info[0] == 2 else kiter1100)
                oprot.writeString(viter1101.encode('utf-8') if sys.version_info[0] == 2 else viter1101)
            oprot.writeMapEnd()
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
all_structs.append(updateBuddyProfileAttributes_args)
updateBuddyProfileAttributes_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.MAP, 'attributes', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)


class updateBuddyProfileAttributes_result(object):
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
                    self.success = UpdateBuddyProfileResult()
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
        oprot.writeStructBegin('updateBuddyProfileAttributes_result')
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
all_structs.append(updateBuddyProfileAttributes_result)
updateBuddyProfileAttributes_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [UpdateBuddyProfileResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddyProfileAttributesAsync_args(object):
    """
    Attributes:
     - requestId
     - attributes
    """


    def __init__(self, requestId=None, attributes=None,):
        self.requestId = requestId
        self.attributes = attributes

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.attributes = {}
                    (_ktype1103, _vtype1104, _size1102) = iprot.readMapBegin()
                    for _i1106 in range(_size1102):
                        _key1107 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val1108 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.attributes[_key1107] = _val1108
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('updateBuddyProfileAttributesAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.attributes is not None:
            oprot.writeFieldBegin('attributes', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.attributes))
            for kiter1109, viter1110 in self.attributes.items():
                oprot.writeString(kiter1109.encode('utf-8') if sys.version_info[0] == 2 else kiter1109)
                oprot.writeString(viter1110.encode('utf-8') if sys.version_info[0] == 2 else viter1110)
            oprot.writeMapEnd()
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
all_structs.append(updateBuddyProfileAttributesAsync_args)
updateBuddyProfileAttributesAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.MAP, 'attributes', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)


class updateBuddyProfileAttributesAsync_result(object):
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
        oprot.writeStructBegin('updateBuddyProfileAttributesAsync_result')
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
all_structs.append(updateBuddyProfileAttributesAsync_result)
updateBuddyProfileAttributesAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddyProfileImage_args(object):
    """
    Attributes:
     - requestId
     - image
    """


    def __init__(self, requestId=None, image=None,):
        self.requestId = requestId
        self.image = image

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.image = iprot.readBinary()
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
        oprot.writeStructBegin('updateBuddyProfileImage_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.image is not None:
            oprot.writeFieldBegin('image', TType.STRING, 2)
            oprot.writeBinary(self.image)
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
all_structs.append(updateBuddyProfileImage_args)
updateBuddyProfileImage_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'image', 'BINARY', None, ),  # 2
)


class updateBuddyProfileImage_result(object):
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
                    self.success = UpdateBuddyProfileResult()
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
        oprot.writeStructBegin('updateBuddyProfileImage_result')
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
all_structs.append(updateBuddyProfileImage_result)
updateBuddyProfileImage_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [UpdateBuddyProfileResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddyProfileImageAsync_args(object):
    """
    Attributes:
     - requestId
     - image
    """


    def __init__(self, requestId=None, image=None,):
        self.requestId = requestId
        self.image = image

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.image = iprot.readBinary()
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
        oprot.writeStructBegin('updateBuddyProfileImageAsync_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.image is not None:
            oprot.writeFieldBegin('image', TType.STRING, 2)
            oprot.writeBinary(self.image)
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
all_structs.append(updateBuddyProfileImageAsync_args)
updateBuddyProfileImageAsync_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'image', 'BINARY', None, ),  # 2
)


class updateBuddyProfileImageAsync_result(object):
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
        oprot.writeStructBegin('updateBuddyProfileImageAsync_result')
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
all_structs.append(updateBuddyProfileImageAsync_result)
updateBuddyProfileImageAsync_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddySearchId_args(object):
    """
    Attributes:
     - requestId
     - searchId
    """


    def __init__(self, requestId=None, searchId=None,):
        self.requestId = requestId
        self.searchId = searchId

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.searchId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('updateBuddySearchId_args')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.searchId is not None:
            oprot.writeFieldBegin('searchId', TType.STRING, 2)
            oprot.writeString(self.searchId.encode('utf-8') if sys.version_info[0] == 2 else self.searchId)
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
all_structs.append(updateBuddySearchId_args)
updateBuddySearchId_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'searchId', 'UTF8', None, ),  # 2
)


class updateBuddySearchId_result(object):
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
        oprot.writeStructBegin('updateBuddySearchId_result')
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
all_structs.append(updateBuddySearchId_result)
updateBuddySearchId_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class updateBuddySettings_args(object):
    """
    Attributes:
     - settings
    """


    def __init__(self, settings=None,):
        self.settings = settings

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
                if ftype == TType.MAP:
                    self.settings = {}
                    (_ktype1112, _vtype1113, _size1111) = iprot.readMapBegin()
                    for _i1115 in range(_size1111):
                        _key1116 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val1117 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.settings[_key1116] = _val1117
                    iprot.readMapEnd()
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
        oprot.writeStructBegin('updateBuddySettings_args')
        if self.settings is not None:
            oprot.writeFieldBegin('settings', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.settings))
            for kiter1118, viter1119 in self.settings.items():
                oprot.writeString(kiter1118.encode('utf-8') if sys.version_info[0] == 2 else kiter1118)
                oprot.writeString(viter1119.encode('utf-8') if sys.version_info[0] == 2 else viter1119)
            oprot.writeMapEnd()
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
all_structs.append(updateBuddySettings_args)
updateBuddySettings_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.MAP, 'settings', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)


class updateBuddySettings_result(object):
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
        oprot.writeStructBegin('updateBuddySettings_result')
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
all_structs.append(updateBuddySettings_result)
updateBuddySettings_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class uploadBuddyContent_args(object):
    """
    Attributes:
     - contentType
     - content
    """


    def __init__(self, contentType=None, content=None,):
        self.contentType = contentType
        self.content = content

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
                    self.contentType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.content = iprot.readBinary()
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
        oprot.writeStructBegin('uploadBuddyContent_args')
        if self.contentType is not None:
            oprot.writeFieldBegin('contentType', TType.I32, 2)
            oprot.writeI32(self.contentType)
            oprot.writeFieldEnd()
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.STRING, 3)
            oprot.writeBinary(self.content)
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
all_structs.append(uploadBuddyContent_args)
uploadBuddyContent_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.I32, 'contentType', None, None, ),  # 2
    (3, TType.STRING, 'content', 'BINARY', None, ),  # 3
)


class uploadBuddyContent_result(object):
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
        oprot.writeStructBegin('uploadBuddyContent_result')
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
all_structs.append(uploadBuddyContent_result)
uploadBuddyContent_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
#fix_spec(all_structs)
del all_structs

