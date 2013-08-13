import irssi
import logging
import graypy
import re

log = logging.getLogger()
log.setLevel(logging.DEBUG)
handler = graypy.GELFHandler('localhost', 12201, debugging_fields=False)
#handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))

log.addHandler(handler)


def stripColors(msg):
    pattern = re.compile("\x1f|\x02|\x12|\x0f|\x16|\x03(?:\d{1,2}(?:,\d{1,2})?)?",
            re.UNICODE)
    return re.sub(pattern,'',msg)

def testlog(server, data, nick, mask, target):
    log.info("%s %s %s %s %s" %
            (server.tag, target, nick, mask,  stripColors(data)))



irssi.signal_add('message public',testlog)
