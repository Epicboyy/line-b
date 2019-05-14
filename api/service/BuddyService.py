from ..ThriftService import *
import sys
import logging
from .ttypes import *

all_structs = []


class Iface(object):
    def findBuddyContactsByQuery(self, language, country, query, fromIndex, count, requestSource):
        """
        Parameters:
         - language
         - country
         - query
         - fromIndex
         - count
         - requestSource
        """
        pass

    def getBuddyContacts(self, language, country, classification, fromIndex, count):
        """
        Parameters:
         - language
         - country
         - classification
         - fromIndex
         - count
        """
        pass

    def getBuddyDetail(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getBuddyOnAir(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        pass

    def getCountriesHavingBuddy(self):
        pass

    def getNewlyReleasedBuddyIds(self, country):
        """
        Parameters:
         - country
        """
        pass

    def getPopularBuddyBanner(self, language, country, applicationType, resourceSpecification):
        """
        Parameters:
         - language
         - country
         - applicationType
         - resourceSpecification
        """
        pass

    def getPopularBuddyLists(self, language, country):
        """
        Parameters:
         - language
         - country
        """
        pass

    def getPromotedBuddyContacts(self, language, country):
        """
        Parameters:
         - language
         - country
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def findBuddyContactsByQuery(self, language, country, query, fromIndex, count, requestSource):
        """
        Parameters:
         - language
         - country
         - query
         - fromIndex
         - count
         - requestSource
        """
        self.send_findBuddyContactsByQuery(language, country, query, fromIndex, count, requestSource)
        return self.recv_findBuddyContactsByQuery()

    def send_findBuddyContactsByQuery(self, language, country, query, fromIndex, count, requestSource):
        self._oprot.writeMessageBegin('findBuddyContactsByQuery', TMessageType.CALL, self._seqid)
        args = findBuddyContactsByQuery_args()
        args.language = language
        args.country = country
        args.query = query
        args.fromIndex = fromIndex
        args.count = count
        args.requestSource = requestSource
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_findBuddyContactsByQuery(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = findBuddyContactsByQuery_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "findBuddyContactsByQuery failed: unknown result")

    def getBuddyContacts(self, language, country, classification, fromIndex, count):
        """
        Parameters:
         - language
         - country
         - classification
         - fromIndex
         - count
        """
        self.send_getBuddyContacts(language, country, classification, fromIndex, count)
        return self.recv_getBuddyContacts()

    def send_getBuddyContacts(self, language, country, classification, fromIndex, count):
        self._oprot.writeMessageBegin('getBuddyContacts', TMessageType.CALL, self._seqid)
        args = getBuddyContacts_args()
        args.language = language
        args.country = country
        args.classification = classification
        args.fromIndex = fromIndex
        args.count = count
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBuddyContacts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBuddyContacts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBuddyContacts failed: unknown result")

    def getBuddyDetail(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_getBuddyDetail(buddyMid)
        return self.recv_getBuddyDetail()

    def send_getBuddyDetail(self, buddyMid):
        self._oprot.writeMessageBegin('getBuddyDetail', TMessageType.CALL, self._seqid)
        args = getBuddyDetail_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBuddyDetail(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBuddyDetail_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBuddyDetail failed: unknown result")

    def getBuddyOnAir(self, buddyMid):
        """
        Parameters:
         - buddyMid
        """
        self.send_getBuddyOnAir(buddyMid)
        return self.recv_getBuddyOnAir()

    def send_getBuddyOnAir(self, buddyMid):
        self._oprot.writeMessageBegin('getBuddyOnAir', TMessageType.CALL, self._seqid)
        args = getBuddyOnAir_args()
        args.buddyMid = buddyMid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getBuddyOnAir(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getBuddyOnAir_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getBuddyOnAir failed: unknown result")

    def getCountriesHavingBuddy(self):
        self.send_getCountriesHavingBuddy()
        return self.recv_getCountriesHavingBuddy()

    def send_getCountriesHavingBuddy(self):
        self._oprot.writeMessageBegin('getCountriesHavingBuddy', TMessageType.CALL, self._seqid)
        args = getCountriesHavingBuddy_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getCountriesHavingBuddy(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getCountriesHavingBuddy_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getCountriesHavingBuddy failed: unknown result")

    def getNewlyReleasedBuddyIds(self, country):
        """
        Parameters:
         - country
        """
        self.send_getNewlyReleasedBuddyIds(country)
        return self.recv_getNewlyReleasedBuddyIds()

    def send_getNewlyReleasedBuddyIds(self, country):
        self._oprot.writeMessageBegin('getNewlyReleasedBuddyIds', TMessageType.CALL, self._seqid)
        args = getNewlyReleasedBuddyIds_args()
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getNewlyReleasedBuddyIds(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getNewlyReleasedBuddyIds_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getNewlyReleasedBuddyIds failed: unknown result")

    def getPopularBuddyBanner(self, language, country, applicationType, resourceSpecification):
        """
        Parameters:
         - language
         - country
         - applicationType
         - resourceSpecification
        """
        self.send_getPopularBuddyBanner(language, country, applicationType, resourceSpecification)
        return self.recv_getPopularBuddyBanner()

    def send_getPopularBuddyBanner(self, language, country, applicationType, resourceSpecification):
        self._oprot.writeMessageBegin('getPopularBuddyBanner', TMessageType.CALL, self._seqid)
        args = getPopularBuddyBanner_args()
        args.language = language
        args.country = country
        args.applicationType = applicationType
        args.resourceSpecification = resourceSpecification
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPopularBuddyBanner(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPopularBuddyBanner_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPopularBuddyBanner failed: unknown result")

    def getPopularBuddyLists(self, language, country):
        """
        Parameters:
         - language
         - country
        """
        self.send_getPopularBuddyLists(language, country)
        return self.recv_getPopularBuddyLists()

    def send_getPopularBuddyLists(self, language, country):
        self._oprot.writeMessageBegin('getPopularBuddyLists', TMessageType.CALL, self._seqid)
        args = getPopularBuddyLists_args()
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPopularBuddyLists(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPopularBuddyLists_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPopularBuddyLists failed: unknown result")

    def getPromotedBuddyContacts(self, language, country):
        """
        Parameters:
         - language
         - country
        """
        self.send_getPromotedBuddyContacts(language, country)
        return self.recv_getPromotedBuddyContacts()

    def send_getPromotedBuddyContacts(self, language, country):
        self._oprot.writeMessageBegin('getPromotedBuddyContacts', TMessageType.CALL, self._seqid)
        args = getPromotedBuddyContacts_args()
        args.language = language
        args.country = country
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_getPromotedBuddyContacts(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = getPromotedBuddyContacts_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "getPromotedBuddyContacts failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["findBuddyContactsByQuery"] = Processor.process_findBuddyContactsByQuery
        self._processMap["getBuddyContacts"] = Processor.process_getBuddyContacts
        self._processMap["getBuddyDetail"] = Processor.process_getBuddyDetail
        self._processMap["getBuddyOnAir"] = Processor.process_getBuddyOnAir
        self._processMap["getCountriesHavingBuddy"] = Processor.process_getCountriesHavingBuddy
        self._processMap["getNewlyReleasedBuddyIds"] = Processor.process_getNewlyReleasedBuddyIds
        self._processMap["getPopularBuddyBanner"] = Processor.process_getPopularBuddyBanner
        self._processMap["getPopularBuddyLists"] = Processor.process_getPopularBuddyLists
        self._processMap["getPromotedBuddyContacts"] = Processor.process_getPromotedBuddyContacts

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

    def process_findBuddyContactsByQuery(self, seqid, iprot, oprot):
        args = findBuddyContactsByQuery_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = findBuddyContactsByQuery_result()
        try:
            result.success = self._handler.findBuddyContactsByQuery(args.language, args.country, args.query, args.fromIndex, args.count, args.requestSource)
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
        oprot.writeMessageBegin("findBuddyContactsByQuery", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBuddyContacts(self, seqid, iprot, oprot):
        args = getBuddyContacts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBuddyContacts_result()
        try:
            result.success = self._handler.getBuddyContacts(args.language, args.country, args.classification, args.fromIndex, args.count)
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
        oprot.writeMessageBegin("getBuddyContacts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBuddyDetail(self, seqid, iprot, oprot):
        args = getBuddyDetail_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBuddyDetail_result()
        try:
            result.success = self._handler.getBuddyDetail(args.buddyMid)
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
        oprot.writeMessageBegin("getBuddyDetail", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getBuddyOnAir(self, seqid, iprot, oprot):
        args = getBuddyOnAir_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getBuddyOnAir_result()
        try:
            result.success = self._handler.getBuddyOnAir(args.buddyMid)
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
        oprot.writeMessageBegin("getBuddyOnAir", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getCountriesHavingBuddy(self, seqid, iprot, oprot):
        args = getCountriesHavingBuddy_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getCountriesHavingBuddy_result()
        try:
            result.success = self._handler.getCountriesHavingBuddy()
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
        oprot.writeMessageBegin("getCountriesHavingBuddy", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getNewlyReleasedBuddyIds(self, seqid, iprot, oprot):
        args = getNewlyReleasedBuddyIds_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getNewlyReleasedBuddyIds_result()
        try:
            result.success = self._handler.getNewlyReleasedBuddyIds(args.country)
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
        oprot.writeMessageBegin("getNewlyReleasedBuddyIds", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPopularBuddyBanner(self, seqid, iprot, oprot):
        args = getPopularBuddyBanner_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPopularBuddyBanner_result()
        try:
            result.success = self._handler.getPopularBuddyBanner(args.language, args.country, args.applicationType, args.resourceSpecification)
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
        oprot.writeMessageBegin("getPopularBuddyBanner", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPopularBuddyLists(self, seqid, iprot, oprot):
        args = getPopularBuddyLists_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPopularBuddyLists_result()
        try:
            result.success = self._handler.getPopularBuddyLists(args.language, args.country)
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
        oprot.writeMessageBegin("getPopularBuddyLists", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_getPromotedBuddyContacts(self, seqid, iprot, oprot):
        args = getPromotedBuddyContacts_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPromotedBuddyContacts_result()
        try:
            result.success = self._handler.getPromotedBuddyContacts(args.language, args.country)
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
        oprot.writeMessageBegin("getPromotedBuddyContacts", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class findBuddyContactsByQuery_args(object):
    """
    Attributes:
     - language
     - country
     - query
     - fromIndex
     - count
     - requestSource
    """


    def __init__(self, language=None, country=None, query=None, fromIndex=None, count=None, requestSource=None,):
        self.language = language
        self.country = country
        self.query = query
        self.fromIndex = fromIndex
        self.count = count
        self.requestSource = requestSource

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
            elif fid == 3:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.query = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.fromIndex = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.requestSource = iprot.readI32()
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
        oprot.writeStructBegin('findBuddyContactsByQuery_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 3)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.query is not None:
            oprot.writeFieldBegin('query', TType.STRING, 4)
            oprot.writeString(self.query.encode('utf-8') if sys.version_info[0] == 2 else self.query)
            oprot.writeFieldEnd()
        if self.fromIndex is not None:
            oprot.writeFieldBegin('fromIndex', TType.I32, 5)
            oprot.writeI32(self.fromIndex)
            oprot.writeFieldEnd()
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I32, 6)
            oprot.writeI32(self.count)
            oprot.writeFieldEnd()
        if self.requestSource is not None:
            oprot.writeFieldBegin('requestSource', TType.I32, 7)
            oprot.writeI32(self.requestSource)
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
all_structs.append(findBuddyContactsByQuery_args)
findBuddyContactsByQuery_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'country', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'query', 'UTF8', None, ),  # 4
    (5, TType.I32, 'fromIndex', None, None, ),  # 5
    (6, TType.I32, 'count', None, None, ),  # 6
    (7, TType.I32, 'requestSource', None, None, ),  # 7
)


class findBuddyContactsByQuery_result(object):
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
                    (_etype1123, _size1120) = iprot.readListBegin()
                    for _i1124 in range(_size1120):
                        _elem1125 = BuddySearchResult()
                        _elem1125.read(iprot)
                        self.success.append(_elem1125)
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
        oprot.writeStructBegin('findBuddyContactsByQuery_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1126 in self.success:
                iter1126.write(oprot)
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
all_structs.append(findBuddyContactsByQuery_result)
findBuddyContactsByQuery_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [BuddySearchResult, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBuddyContacts_args(object):
    """
    Attributes:
     - language
     - country
     - classification
     - fromIndex
     - count
    """


    def __init__(self, language=None, country=None, classification=None, fromIndex=None, count=None,):
        self.language = language
        self.country = country
        self.classification = classification
        self.fromIndex = fromIndex
        self.count = count

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
            elif fid == 3:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.classification = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.fromIndex = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
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
        oprot.writeStructBegin('getBuddyContacts_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 3)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.classification is not None:
            oprot.writeFieldBegin('classification', TType.STRING, 4)
            oprot.writeString(self.classification.encode('utf-8') if sys.version_info[0] == 2 else self.classification)
            oprot.writeFieldEnd()
        if self.fromIndex is not None:
            oprot.writeFieldBegin('fromIndex', TType.I32, 5)
            oprot.writeI32(self.fromIndex)
            oprot.writeFieldEnd()
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I32, 6)
            oprot.writeI32(self.count)
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
all_structs.append(getBuddyContacts_args)
getBuddyContacts_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'country', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'classification', 'UTF8', None, ),  # 4
    (5, TType.I32, 'fromIndex', None, None, ),  # 5
    (6, TType.I32, 'count', None, None, ),  # 6
)


class getBuddyContacts_result(object):
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
                    (_etype1130, _size1127) = iprot.readListBegin()
                    for _i1131 in range(_size1127):
                        _elem1132 = Contact()
                        _elem1132.read(iprot)
                        self.success.append(_elem1132)
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
        oprot.writeStructBegin('getBuddyContacts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1133 in self.success:
                iter1133.write(oprot)
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
all_structs.append(getBuddyContacts_result)
getBuddyContacts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [Contact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBuddyDetail_args(object):
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
            if fid == 4:
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
        oprot.writeStructBegin('getBuddyDetail_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 4)
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
all_structs.append(getBuddyDetail_args)
getBuddyDetail_args.thrift_spec = (
    None,  # 0
    None,  # 1
    None,  # 2
    None,  # 3
    (4, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 4
)


class getBuddyDetail_result(object):
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
        oprot.writeStructBegin('getBuddyDetail_result')
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
all_structs.append(getBuddyDetail_result)
getBuddyDetail_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BuddyDetail, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getBuddyOnAir_args(object):
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
            if fid == 4:
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
        oprot.writeStructBegin('getBuddyOnAir_args')
        if self.buddyMid is not None:
            oprot.writeFieldBegin('buddyMid', TType.STRING, 4)
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
all_structs.append(getBuddyOnAir_args)
getBuddyOnAir_args.thrift_spec = (
    None,  # 0
    None,  # 1
    None,  # 2
    None,  # 3
    (4, TType.STRING, 'buddyMid', 'UTF8', None, ),  # 4
)


class getBuddyOnAir_result(object):
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
                    self.success = BuddyOnAir()
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
        oprot.writeStructBegin('getBuddyOnAir_result')
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
all_structs.append(getBuddyOnAir_result)
getBuddyOnAir_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BuddyOnAir, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getCountriesHavingBuddy_args(object):


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
        oprot.writeStructBegin('getCountriesHavingBuddy_args')
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
all_structs.append(getCountriesHavingBuddy_args)
getCountriesHavingBuddy_args.thrift_spec = (
)


class getCountriesHavingBuddy_result(object):
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
                    (_etype1137, _size1134) = iprot.readListBegin()
                    for _i1138 in range(_size1134):
                        _elem1139 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success.append(_elem1139)
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
        oprot.writeStructBegin('getCountriesHavingBuddy_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter1140 in self.success:
                oprot.writeString(iter1140.encode('utf-8') if sys.version_info[0] == 2 else iter1140)
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
all_structs.append(getCountriesHavingBuddy_result)
getCountriesHavingBuddy_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getNewlyReleasedBuddyIds_args(object):
    """
    Attributes:
     - country
    """


    def __init__(self, country=None,):
        self.country = country

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
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getNewlyReleasedBuddyIds_args')
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 3)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getNewlyReleasedBuddyIds_args)
getNewlyReleasedBuddyIds_args.thrift_spec = (
    None,  # 0
    None,  # 1
    None,  # 2
    (3, TType.STRING, 'country', 'UTF8', None, ),  # 3
)


class getNewlyReleasedBuddyIds_result(object):
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
                    (_ktype1142, _vtype1143, _size1141) = iprot.readMapBegin()
                    for _i1145 in range(_size1141):
                        _key1146 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val1147 = iprot.readI64()
                        self.success[_key1146] = _val1147
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
        oprot.writeStructBegin('getNewlyReleasedBuddyIds_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.STRING, TType.I64, len(self.success))
            for kiter1148, viter1149 in self.success.items():
                oprot.writeString(kiter1148.encode('utf-8') if sys.version_info[0] == 2 else kiter1148)
                oprot.writeI64(viter1149)
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
all_structs.append(getNewlyReleasedBuddyIds_result)
getNewlyReleasedBuddyIds_result.thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING, 'UTF8', TType.I64, None, False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPopularBuddyBanner_args(object):
    """
    Attributes:
     - language
     - country
     - applicationType
     - resourceSpecification
    """


    def __init__(self, language=None, country=None, applicationType=None, resourceSpecification=None,):
        self.language = language
        self.country = country
        self.applicationType = applicationType
        self.resourceSpecification = resourceSpecification

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
            elif fid == 3:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.applicationType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.resourceSpecification = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getPopularBuddyBanner_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 3)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
            oprot.writeFieldEnd()
        if self.applicationType is not None:
            oprot.writeFieldBegin('applicationType', TType.I32, 4)
            oprot.writeI32(self.applicationType)
            oprot.writeFieldEnd()
        if self.resourceSpecification is not None:
            oprot.writeFieldBegin('resourceSpecification', TType.STRING, 5)
            oprot.writeString(self.resourceSpecification.encode('utf-8') if sys.version_info[0] == 2 else self.resourceSpecification)
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
all_structs.append(getPopularBuddyBanner_args)
getPopularBuddyBanner_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'country', 'UTF8', None, ),  # 3
    (4, TType.I32, 'applicationType', None, None, ),  # 4
    (5, TType.STRING, 'resourceSpecification', 'UTF8', None, ),  # 5
)


class getPopularBuddyBanner_result(object):
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
                    self.success = BuddyBanner()
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
        oprot.writeStructBegin('getPopularBuddyBanner_result')
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
all_structs.append(getPopularBuddyBanner_result)
getPopularBuddyBanner_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BuddyBanner, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPopularBuddyLists_args(object):
    """
    Attributes:
     - language
     - country
    """


    def __init__(self, language=None, country=None,):
        self.language = language
        self.country = country

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
            elif fid == 3:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getPopularBuddyLists_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 3)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getPopularBuddyLists_args)
getPopularBuddyLists_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'country', 'UTF8', None, ),  # 3
)


class getPopularBuddyLists_result(object):
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
                    (_etype1153, _size1150) = iprot.readListBegin()
                    for _i1154 in range(_size1150):
                        _elem1155 = BuddyList()
                        _elem1155.read(iprot)
                        self.success.append(_elem1155)
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
        oprot.writeStructBegin('getPopularBuddyLists_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1156 in self.success:
                iter1156.write(oprot)
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
all_structs.append(getPopularBuddyLists_result)
getPopularBuddyLists_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [BuddyList, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class getPromotedBuddyContacts_args(object):
    """
    Attributes:
     - language
     - country
    """


    def __init__(self, language=None, country=None,):
        self.language = language
        self.country = country

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
            elif fid == 3:
                if ftype == TType.STRING:
                    self.country = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('getPromotedBuddyContacts_args')
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.country is not None:
            oprot.writeFieldBegin('country', TType.STRING, 3)
            oprot.writeString(self.country.encode('utf-8') if sys.version_info[0] == 2 else self.country)
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
all_structs.append(getPromotedBuddyContacts_args)
getPromotedBuddyContacts_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'country', 'UTF8', None, ),  # 3
)


class getPromotedBuddyContacts_result(object):
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
                    (_etype1160, _size1157) = iprot.readListBegin()
                    for _i1161 in range(_size1157):
                        _elem1162 = Contact()
                        _elem1162.read(iprot)
                        self.success.append(_elem1162)
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
        oprot.writeStructBegin('getPromotedBuddyContacts_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter1163 in self.success:
                iter1163.write(oprot)
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
all_structs.append(getPromotedBuddyContacts_result)
getPromotedBuddyContacts_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT, [Contact, None], False), None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
#fix_spec(all_structs)
del all_structs

