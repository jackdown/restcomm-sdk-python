'''
 * TeleStax, Open Source Cloud Communications
 * Copyright 2011-2016, Telestax Inc and individual contributors
 * by the @authors tag.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 '''
import requests
import json

class client(object):

    def __init__(self, Sid, AuthToken, BaseUrl):

        self.Sid = Sid
        self.AuthToken = AuthToken
        self.BaseUrl = BaseUrl

class PhoneNumberList(object):

    def __init__(self, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def GetList(self):

        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/IncomingPhoneNumbers.json'
        r1 = requests.get(Url, auth=(self.Sid, self.AuthToken))
        content = json.loads(r1.text)
        return content

class AttachPhoneNumber(object):

    def __init__(self, phNumber, VoiceUrl, option, client):

        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl
        self.phNumber = phNumber
        self.VoiceUrl = VoiceUrl
        self.option = option

    def Attach(self):

        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/IncomingPhoneNumbers.json'
        data = {'PhoneNumber': self.phNumber, 'VoiceUrl': self.VoiceUrl, 'isSIP': 'true'}
        r2 = requests.post(Url, data=data, auth=(self.Sid, self.AuthToken))
        content = json.loads(r2.text)
        return content

class DeletePhoneNumber(object):

    def __init__(self, CallSid, client):

        self.CallSid = CallSid
        self.Sid = client.Sid
        self.AuthToken = client.AuthToken
        self.BaseUrl = client.BaseUrl

    def Delete(self):

        Url = self.BaseUrl+'/Accounts/'+self.Sid+'/IncomingPhoneNumbers.json/'+self.CallSid
        r3 = requests.delete(Url, auth=(self.Sid, self.AuthToken))
        content = json.loads(r3.text)
        return content