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

from Restcomm_Python_SDk import IncomingNumber
import unittest
import vcr

class TestPhoneNumberList(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_GetList(self):

        try:

                file = open("IncomingNumberData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()

                data = IncomingNumber.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = IncomingNumber.PhoneNumberList(data).GetList()

                self.assertIsNotNone(content)
                file.close()

        except SyntaxError:
            print("Oops! Syntax Error: AccountSid or AuthToken is incorrect. Please check your kind of application also!")
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

class TestAttachPhoneNumber(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Attach(self):

        try:

            file = open("IncomingNumberData.txt", "r")
            Sid = file.readline()
            AuthToken = file.readline()
            BaseUrl = file.readline()
            phNumber = file.readline()
            VoiceUrl = file.readline()
            option = file.readline()

            data = IncomingNumber.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
            content = IncomingNumber.AttachPhoneNumber(phNumber.strip(), VoiceUrl.strip(), option.strip(), data).Attach()

            self.assertIsNotNone(content)
            file.close()

        except SyntaxError:
            print(
                "Oops! Syntax Error: AccountSid or AuthToken is incorrect. Please check your kind of application also!")
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


class TestDeletePhoneNumber(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Delete(self):

        try:

            file = open("IncomingNumberData.txt", "r")
            Sid = file.readline()
            AuthToken = file.readline()
            BaseUrl = file.readline()
            file.readline()
            file.readline()
            file.readline()
            CallSid = file.readline()

            data = IncomingNumber.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
            content = IncomingNumber.DeletePhoneNumber(CallSid.strip(), data).Delete()

            self.assertIsNotNone(content)
            file.close()

        except SyntaxError:
            print(
                "Oops! Syntax Error: AccountSid or AuthToken is incorrect. Please check your kind of application also!")
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