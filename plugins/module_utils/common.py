# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Replicated from amazon.aws because the client agent string will be released
# in amazon.aws 6.0.0

AMAZON_CLOUD_COLLECTION_NAME = "amazon.cloud"
AMAZON_CLOUD_COLLECTION_VERSION = "0.3.0"


_collection_info_context = {
    "name": AMAZON_CLOUD_COLLECTION_NAME,
    "version": AMAZON_CLOUD_COLLECTION_VERSION,
}


def set_collection_info(collection_name=None, collection_version=None):
    if collection_name:
        _collection_info_context["name"] = collection_name
    if collection_version:
        _collection_info_context["version"] = collection_version


def get_collection_info():
    return _collection_info_context
