#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Student(object):

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')

        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')

        self.score = value


s = Student()
s.score = 60


