# Title     : TODO
# Objective : TODO
# Created by: ringtail
# Created on: 2019/3/7


from __future__ import absolute_import, division, print_function

from derrick.core.detector import Detector
from derrick.core.logger import Logger
import os
import yaml


# Parse config from baas
class BaasFileDetector(Detector):
    def execute(self, *args, **kwargs):
        cwd = os.getcwd()
        file_path = os.path.join(cwd, "baas.yaml")
        try:
            f = open(file_path, "r")
            res = yaml.safe_load(f)
            if self.check_valid(res) is not True:
                Logger.error("You must specific those required keys.")
                exit(-1)
            return res
        except Exception as e:
            Logger.error("Failed to load yaml file from disk,because of %s" % e.message)
            exit(-1)
        finally:
            f.close()

    # check yaml valid
    @staticmethod
    def check_valid(y):
        if y["project_name"] == "" or y["base_image"] == "" or y["image_with_tag"] == "" or y["jar_file"] == "":
            Logger.error("Failed to valid yaml file, "
                         "required keys are project_name: %s base_image: %s image_with_tag: %s jar_file: %s" %
                         y["project_name"], y["base_image"], y["image_with_tag"], y["jar_file"])
            return False
        return True
