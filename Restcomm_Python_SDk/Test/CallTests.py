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

from Restcomm_Python_SDk import call
import unittest
import vcr

class TestMakeCall(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def testCall(self):

        try:

                file = open("CallData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                From = file.readline()
                To = file.readline()
                Url = file.readline()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.Makecall(From.strip(), To.strip(), Url.strip(), data).Call()

                self.assertIsNotNone(content)
                file.close()


        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestGetCallDetails(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_GetDetails(self):

        try:

                file = open("CallData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.GetCallDetail(data).GetDetails()

                self.assertIsNotNone(content)
                file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("TypeError: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestRedirectCall(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Redirect(self):

        try:

                file = open("CallData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                Url = file.readline()
                SubSid = file.readline()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.RedirectCall(Url.strip(), SubSid.strip(), data).Redirect()

                self.assertIsNotNone(content)
                file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("TimeoutError: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestConferenceCall(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Conference(self):

        try:

                file = open("CallData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                Url = file.readline()
                SubSid = file.readline()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.ConferenceCall(Url.strip(), SubSid.strip(), data).Conference()

                self.assertIsNotNone(content)
                file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

class TestMuteCall(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Mute(self):

        try:

                file = open("CallData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                PartSid = file.readline()
                ConSid = file.readline()

                data = call.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = call.MuteParticipant(PartSid.strip(), ConSid.strip(), data).Mute()

                self.assertIsNotNone(content)
                file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")


class TestUnMuteCall(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Mute(self):

        try:

                file = open("CallData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                file.readline()
                PartSid = file.readline()
                ConSid = file.readline()

                data = call.client(Sid.strip(), AuthToken.strip())
                content = call.UnMuteParticipant(PartSid.strip(), ConSid.strip(), data).UnMute()

                self.assertIsNotNone(content)
                file.close()

        except SyntaxError:
            print("Oops! Syntax Error: it seems your AccountSid or AuthToken is incorrect or you are not logged in!")
        except ConnectionError:
            print("Connection Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Timeout Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")
        except IndexError:
            print("Index Error: list Index out of range")

if __name__ == '__main__':
    unittest.main()