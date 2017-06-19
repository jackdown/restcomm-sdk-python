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

from Restcomm_Python_SDk import Applications
import unittest
import vcr

class TestCreateApplication(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Create(self):

        try:

                file = open("ApplicationData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                FriendlyName = file.readline()
                kind = file.readline()


                data = Applications.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Applications.CreateApplication(FriendlyName.strip(), kind.strip(), data).Create()

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

class TestGetApplicationDetail(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_GetDetail(self):

        try:

                file = open("ApplicationData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()


                data = Applications.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Applications.GetApplicationList(data).GetList()

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
        except IndexError:
            print("Index Error: list Index out of range")
        except TypeError:
            print("Type Error: the value is of wrong type")

class TestDeleteApplication(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Delete(self):

        try:

                file = open("ApplicationData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                AppSid = file.readline()

                data = Applications.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Applications.DeleteApplication(AppSid.strip(), data)

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

class TestUpdateApplication(unittest.TestCase):

    @vcr.use_cassette(record_mode='new_episodes')
    def test_Update(self):

        try:

                file = open("ApplicationData.txt","r")
                Sid = file.readline()
                AuthToken = file.readline()
                BaseUrl = file.readline()
                file.readline()
                file.readline()
                AppSid = file.readline()
                FriendlyName = file.readline()

                data = Applications.client(Sid.strip(), AuthToken.strip(), BaseUrl.strip())
                content = Applications.UpdateApplication(AppSid.strip(), FriendlyName.strip(), data)

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
            print("Type Error: the value is of wrong type!")

if __name__=="__main__":
    unittest.main()
