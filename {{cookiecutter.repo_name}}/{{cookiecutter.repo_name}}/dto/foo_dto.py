# -*- coding: utf-8 -*-

"""Copyright Header Details

Copyright
---------
    Copyright (C) Guya , PLC - All Rights Reserved (As Of Pending...)
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential

LICENSE
-------
    This file is subject to the terms and conditions defined in
    file 'LICENSE.txt', which is part of this source code package.

Authors
-------
    * [Simon Belete](https://github.com/Simonbelete)
 
Project
-------
    * Name: 
        - Guya E-commerce & Guya Express
    * Sub Project Name:
        - {{cookiecutter.project_name}}
    * Description
        - {{cookiecutter.description}}
"""


from flask_restplus import Namespace, fields

from {{cookiecutter.repo_name}}.blueprint.v1.foo import namespace


class FooDto:
    """Request and Respons Data Transfer Object."""

    request = namespace.model('foo_request', {})

    response = namespace.model('foo_response', {})