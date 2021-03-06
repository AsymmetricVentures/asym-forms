# -*- coding: utf-8 -*-
#    Asymmetric Base Framework - A collection of utilities for django frameworks
#    Copyright (C) 2013  Asymmetric Ventures Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import absolute_import, division, print_function, unicode_literals

from django import forms

class ExtendedModelMultipleChoiceField(forms.ModelMultipleChoiceField):
	''' Works the same as a ModelMultipleChoiceField except that it works
		in tandom with fielditerator to provide the model instance that the
		choice is representing
	'''
	
	def prepare_value(self, value):
		if hasattr(value, '_meta'):
			return (value, super(ExtendedModelMultipleChoiceField, self).prepare_value(value))
		return super(ExtendedModelMultipleChoiceField, self).prepare_value(value)
