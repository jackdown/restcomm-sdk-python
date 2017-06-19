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

from Restcomm_Python_SDk import AccountInfo
import unittest
import vcr

class TestAccountDetails(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_details(self):

        try:

                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()

                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.AccountDetails(data).Details()
                self.assertIsNotNone(content)
                file.close()

        except SyntaxError:
            print("Oops! Syntax Error: AccountSid or AuthToken is incorrect!")
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


class TestChangeAccountPassword(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Password(self):

        try:

                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                Password = file.readline()

                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.ChangeAccountPassword(Password.strip(), data).ChangePassword()

                self.assertIsNotNone(content)
                file.close()


        except SyntaxError:
            print("Oops! Syntax Error: AccountSid or AuthToken is incorrect!")
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

class TestCreateSubAccount(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Create(self):

        try:


                file = open("AccountData.txt", "r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                Password = file.readline()
                FriendlyName = file.readline()
                Email = file.readline()


                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.CreateSubAccount(FriendlyName.strip(), Email.strip(), Password.strip(), data)
                self.assertIsNotNone(content)
                file.close()


        except SyntaxError:
            print("Oops! Syntax Error: it seems like your Username/Email-ID is already in use. Please also check your AccountSid/AuthToken!")
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

class TestCloseSubAccount(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Close(self):

        try:


                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                file.readline()
                SubSid = file.readline()


                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl)
                content = AccountInfo.CloseSubAccount(SubSid.strip(), data).Close()

                self.assertIsNotNone(content)
                file.close()


        except SyntaxError:
            print("Oops! Syntax Error: it seems like your Username/Email-ID is already in use. Please also check your AccountSid/AuthToken!")
        except ConnectionError:
            print("Syntax Error: It seems that you have No Connection. Please try again after reconnecting")
        except TimeoutError:
            print("Syntax Error: Its taking too much time")
        except FileNotFoundError:
            print("FileNotFound Error: File not found. please check and try again!")
        except ImportError:
            print("Import Error: Please Import proper library!")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestSubAccountDetails(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Details(self):

        try:

                file = open("AccountData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()

                data = AccountInfo.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = AccountInfo.SubAccountDetails(data).Details()

                self.assertIsNotNone(content)
                file.close()


        except SyntaxError:
            print("Oops! Syntax Error: it seems like your Username/Email-ID is already in use. Please also check your AccountSid/AuthToken!")
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

if __name__=="__main__":
    unittest.main()

