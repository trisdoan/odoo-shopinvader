====================
Shopinvader API Cart
====================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:710a22c613d134c190c084412d51a2ca88f16d568c3499de09288ecd2ceaaaf3
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-shopinvader%2Fodoo--shopinvader-lightgray.png?logo=github
    :target: https://github.com/shopinvader/odoo-shopinvader/tree/16.0/shopinvader_api_cart
    :alt: shopinvader/odoo-shopinvader

|badge1| |badge2| |badge3|

This addon adds a web API on top of the sale.order model to ease the creation of
sale orders from Web frontend. The API is designed to work with the shopinvader-js-cart library
see (https://github.com/shopinvader/shopinvader-js-cart)

**Table of contents**

.. contents::
   :local:

Usage
=====

All the routes under the `cart_router` must be prefixed with `/cart`.
This is not done in this addon to let the developper mount
this router as a sub-app, allowing a specific authentification mechanism.

If mounting the router in the same app as other routers (because it doesn't need a specific authentification mechanism), just add a prefix:

 .. code-block:: python

    def _get_app(self):
       app = super()._get_app()
       app.include_router(router=cart_router, prefix='/cart')
       return app

If you want a nested app, just do as follows:

 .. code-block:: python

    def _get_app(self):
        app = super()._get_app()
        app.dependencies_overrides.update(
            self._get_app_dependencies_overrides()
        )
        cart_app = FastAPI()
        cart_app.include_router(cart_router)
        # First copy dependencies overrides from the main app
        cart_app.dependencies_overrides.update(
            self._get_app_dependencies_overrides()
        )
        # Then add / modify specific dependencies overrides
        cart_app.dependencies_overrides.update(
             self._get_cart_app_dependencies_overrides()
        )
        app.mount("/cart", cart_app)
        return app

Changelog
=========

16.0.1.0.2 (2023-10-13)
~~~~~~~~~~~~~~~~~~~~~~~

**Misc**

- `#1422 <https://github.com/shopinvader/odoo-shopinvader/issues/1422>`_

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/shopinvader/odoo-shopinvader/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/shopinvader/odoo-shopinvader/issues/new?body=module:%20shopinvader_api_cart%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ACSONE SA/NV

Contributors
~~~~~~~~~~~~

* Laurent Mignon <laurent.mignon@acsone.eu>
* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* Marie Lejeune <marie.lejeune@acsone.eu>

Maintainers
~~~~~~~~~~~

This module is part of the `shopinvader/odoo-shopinvader <https://github.com/shopinvader/odoo-shopinvader/tree/16.0/shopinvader_api_cart>`_ project on GitHub.

You are welcome to contribute.
