# -*- coding: utf-8 -*-

import ConfigParser
import codecs
import datetime
import json
import collections


def dict2json(dict):
    return json.dumps(dict, indent=4, separators=(',', ':'), ensure_ascii=False)


def output(fname, value):
    f = codecs.open(fname, "w", "utf-8")
    f.write(value)
    f.close()


def u(obj, key, value):
    return unicode(obj.get(key, value), "utf-8")


if __name__ == "__main__":
    
    # get now time
    d = datetime.datetime.today()
    nowtime = str(d.year) + "-" + str(d.month) + "-" + str(d.day)

    # include config file
    o = ConfigParser.SafeConfigParser()
    o.read("./config.ini")

    # dictionary to json
    dict = collections.OrderedDict()
    dict["string"] = "man"
    dict["number"] = 28
    dict["user"] = []
    
    dict2 = collections.OrderedDict()
    dict2["a"] = "123"
    dict2["b"] = u(o, "user", "name")
    dict2["c"] = u(o, "user", "japan")

    dict["user"].append(dict2)

    result = dict2json(dict)
    output("dict_" + nowtime + ".json", result)
    print result
