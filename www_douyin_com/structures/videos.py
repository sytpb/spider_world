#!/usr/bin/env python 
# coding:utf-8

from www_douyin_com.structures.base import Base


class Video(Base):

    def __init__(self, **kwargs):
        super().__init__()
        self.id = kwargs.get("id")
        self.desc = kwargs.get("desc")
        self.play_url = kwargs.get('play_url')
        self.create_time = kwargs.get("create_time")
        self.user_info = kwargs.get("user_info")
        self.statistic = kwargs.get("statistic")
        self.music = kwargs.get("music")

    def __repr__(self):
        return "<Video: <%s, %s>>" % (self.id, self.desc[:20].strip() if self.desc else None)

