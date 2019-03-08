#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import, division, print_function

from derrick.core.rigging import Rigging
from derrick.core.detector_report import DetectorReport
from detectors.baas_detector import BaasFileDetector
import os

ANT_CHAIN_BAAS = "BaaS"


class BaasRigging(Rigging):
    def detect(self, context):
        cwd = os.getcwd()
        for filename in os.listdir(cwd):
            if filename == "baas.yaml":
                return True, ANT_CHAIN_BAAS
        return False, ""

    def compile(self, context):
        dr = DetectorReport()

        meta = dr.create_node("Meta")
        meta.register_detector(BaasFileDetector())

        dockerfile_node = dr.create_node("Dockerfile.j2")
        dockerfile_node.register_detector(BaasFileDetector())

        kubernetes_node = dr.create_node("kubernetes-deployment.yaml.j2")
        kubernetes_node.register_detector(BaasFileDetector())

        return dr.generate_report()
