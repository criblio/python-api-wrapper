from cribl.packs import *


def packs_testing(base_url, cribl_auth_token, worker_group):
    packs = get_pack_list(base_url=base_url, cribl_auth_token=cribl_auth_token, worker_group=worker_group)
    packs_list = packs["items"]
    for pack in packs_list:
        if pack["id"] == "HelloPacks":
            response = export_pack_merge_safe(base_url=base_url, cribl_auth_token=cribl_auth_token, pack_id=pack["id"],
                                              save_to_directory="./",
                                              worker_group=worker_group)
            if response is not None and response.status_code != 200:
                if response.text.find("Use a different export mode") != -1:
                    print(f"API responded with error: %s" % json.loads(response.text)["message"])
                    print(f"Attempting to download pack using mode=merge...", end='')
                    # try merge
                    response = export_pack_merge(base_url=base_url, cribl_auth_token=cribl_auth_token,
                                                 pack_id=pack["id"],
                                                 save_to_directory="./",
                                                 worker_group=worker_group)
                    if response.status_code == 200:
                        print(f" successfully downloaded pack %s." % pack["id"])
                    else:
                        print(f" could not download pack %s." % pack["id"])
            else:
                print(f"Successfully downloaded pack %s." % pack["id"])
