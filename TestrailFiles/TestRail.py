"""
TestRail integration
"""
import dotenv, os, testrail
from TestrailFiles import Conf_Reader
#Code to automate test case goes here
import unittest
from time import sleep

from Asserts import PhotoLibraryAsserts
from DriverBuilderMultiple import DriverBuilderAndroid
from InstasizePages import EditorPage
from InstasizePages import GridPage
from PaidFiltersPage import PaidEditorPage
from TryExcepts import TryExcepts



class AryaFilterExportTest(unittest.TestCase):


    def get_testrail_client(self):
        "Get the TestRail account credentials from the testrail.env file"
        testrail_file = os.path.join(os.path.dirname(__file__), 'testrail.env')
        # Get the TestRail Url
        testrail_url = Conf_Reader.get_value(testrail_file, 'TESTRAIL_URL')
        client = testrail.APIClient(testrail_url)
        # Get and set the TestRail User and Password
        client.user = Conf_Reader.get_value(testrail_file, 'TESTRAIL_USER')
        client.password = Conf_Reader.get_value(testrail_file, 'TESTRAIL_PASSWORD')

        return client


    def update_testrail(case_id, run_id, result_flag, msg=""):
        "Update TestRail for a given run_id and case_id"
        update_flag = False
        # Get the TestRail client account details
        client = case_id.get_testrail_client()

        # Update the result in TestRail using send_post function.
        # Parameters for add_result_for_case is the combination of runid and case id.
        # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
        status_id = 1 if result_flag is True else 5

        if run_id is not None:
            try:
                result = client.send_post(
                    'add_result_for_case/%s/%s' % (run_id, case_id),
                    {'status_id': status_id, 'comment': msg})
            except:
                print('Exception in update_testrail() updating TestRail.')
                print('PYTHON SAYS: ')
            else:
                print('Updated test result for case: %s in test run: %s with msg:%s' % (case_id, run_id, msg))

        return update_flag

    def get_project_id(project_name):
        "Get the project ID using project name"
        client = project_name.get_testrail_client()
        project_id = None
        projects = client.send_get('get_projects')
        for project in projects:
            if project['name'] == project_name:
                project_id = project['id']
                # project_found_flag=True
                break
        return project_id

    def get_run_id(test_run_name, project_name):
        "Get the run ID using test name and project name"
        run_id = None
        client = test_run_name.get_testrail_client()
        project_id = test_run_name.get_project_id()
        try:
            test_runs = client.send_get('get_runs/%s' % (project_id))
        except Exception as e:
            print('Exception in update_testrail() updating TestRail.')
            print('PYTHON SAYS: ')
            print(e)
            return None
        else:
            for test_run in test_runs:
                if test_run['name'] == test_run_name:
                    run_id = test_run['id']
                    break
            return run_id

    def test_filter_uploads(self):
        driver_builder = DriverBuilderAndroid()
        driver = driver_builder.driver

        # taps on the + icon
        addPhoto = GridPage(driver)
        addPhoto.addPhotoTap()

        # Asserts collapseIcon is displayed
        collapseIcon = GridPage(driver)
        collapseIcon.collapseIconFind()

        # taps on the native photos container
        tapPhotoContainer = GridPage(driver)
        tapPhotoContainer.photoContainers()

        # Asserts allPhotosButton is displayed
        allPhotosButton = PhotoLibraryAsserts(driver)
        allPhotosButton.allPhotosButton()

        # taps on the top left photo
        tapTopLeftPhoto = GridPage(driver)
        tapTopLeftPhoto.topLeftPhoto()

        # taps on the filter
        filters = PaidEditorPage(driver)
        filters.aryaFilter()

        # Asserts tvFilterLevel is displayed
        tvFilterLevel = PhotoLibraryAsserts(driver)
        tvFilterLevel.tvFilterLevel()

        # taps on share button
        tapShareButton = EditorPage(driver)
        tapShareButton.sharebutton()

        # Taps on Instagram icon
        tapInstagram = GridPage(driver)
        tapInstagram.instagramIcon()

        # Searches for Instagram android popup on bottom of screen
        instagramSystemPopup = TryExcepts(driver)
        instagramSystemPopup.instagramSystemPopup()

        sleep(5)
        driver.back()

        # Asserts the + button is displayed
        addPhoto = GridPage(driver)
        addPhoto.addPhotoFind()

        # Tears down the test
        quitTest = EditorPage(driver)
        quitTest.driverQuit()

        # Update TestRail
        # Update TestRail
        case_id = 125  # Case id of your test case
        if (result_flag):
            msg = "Successfully updated the example form"
        else:
            msg = "Failed to update the example form"
            Test_Rail.update_testrail(case_id, test_run_id, result_flag, msg=msg)

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AryaFilterExportTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


