# -*- coding: utf-8 -*-
# 图片改名字
import os
import shutil

def copy_rename_files(mapping, source_dir, dest_dir):
    # 创建目标目录
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        if os.path.isfile(source_file):
            # 如果文件在字典中有映射，则根据映射修改文件名
            if filename in mapping:
                new_filename = mapping[filename]
                dest_file = os.path.join(dest_dir, new_filename)
                # 复制并重命名文件
                shutil.copy(source_file, dest_file)
                print(f"已将 '{source_file}' 复制并重命名为 '{dest_file}'")
            # else:
            #    print('未找到',filename)
            
def empty_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                # print("已删除文件:", file_path)
        except Exception as e:
            print("删除文件时出错:", e)

if __name__ == "__main__":
    # 字典映射旧文件名到新文件名
    file_mapping = {
        # ------------封面-------------------
        "friend_list_closefriends_qmbg@2x.png" : "friend_list_closefriends_bg@2x.png",
        "friend_list_closefriends_cqbg@2x.png" : "friend_list_longlovefriends_bg@2x.png",
        "friend_list_closefriends_bybg@2x.png" : "friend_list_unswerving_bg@2x.png",
        "friend_list_closefriends_yhbg@2x.png" : "friend_list_eternal_bg@2x.png",
        "friend_list_closefriends_tsbg@2x.png" : "friend_list_angel_bg@2x.png",
        "friend_list_closefriends_wybg@2x.png" : "friends_list_only_bg@2x.png",
        "friend_list_closefriends_ssbg@2x.png" : "friend_list_threelive_bg.png",
        "friend_list_closefriends_fdbg@2x.png" : "friend_list_girlFriend_bg.png",
        # 这个是没有的
        "friend_list_closefriends_jlbg@2x.png" : "friend_list_jl_bg@2x.png",
        "friend_list_closefriends_bbbg@2x.png" : "friends_list_Inseparablefriends_bg.png",
        # 这个是webp
        "friend_list_closefriends_llbg@2x.png" : "friends_list_liulijinzhunfriends_bg@2x.png",
        "friend_list_closefriends_hybg@2x.png" : "friends_list_knot_bg@2x.png",
        "friend_list_closefriends_rybg@2x.png" : "friends_list_sun_moon_stone_bg@2x.png",
        "friend_list_closefriends_fhbg@2x.png" : "friends_list_feng_qiu_huang_bg@2x.png",
        "friend_list_closefriends_xybg@2x.png" : "friend_list_xingxue_bg@2x.png",
        "friend_list_closefriends_xlbg@2x.png" : "friend_list_snowlotus_bg.png",
        "friend_list_closefriends_xdbg@2x.png" : "friend_list_heart_bg@2x.png",
        # -------------正方形的小图-------------
        "friends_unswerving_qmbg@2x.png" : "friends_closefriends_bg@2x.png",
        "friends_unswerving_cqbg@2x.png" : "friends_longlovefriends_bg@2x.png",
        "friends_unswerving_bybg@2x.png" : "friends_unswerving_bg@2x.png",
        "friends_unswerving_yhbg@2x.png" : "friends_eternal_bg@2x.png",
        "friends_unswerving_tsbg@2x.png" : "friends_angel_bg@2x.png",
        "friends_unswerving_wybg@2x.png" : "friends_only_bg@2x.png",
        "friends_unswerving_ssbg@2x.png" : "friends_sansheng_bg@2x.png",
        "friends_unswerving_fdbg@2x.png" : "friends_girlFriend_bg@2x.png",
        "friends_unswerving_jlbg@2x.png" : "friends_jinlanfriends_bg@2x.png",
        "friends_unswerving_bbbg@2x.png" : "friends_biyifriends_bg@2x.png",
        "friends_unswerving_llbg@2x.png" : "friends_liulijinzhunfriends_bg@2x.png",
        "friends_unswerving_hybg@2x.png" : "friends_huayufriends_bg@2x.png",
        "friends_unswerving_rybg@2x.png" : "friends_sun_moon_stone_friends_bg@2x.png",
        "friends_unswerving_fhbg@2x.png" : "friends_fengqiuhuang_friends_bg@2x.png",
        "friends_unswerving_xybg@2x.png" : "friends_xingyue_friends_bg@2x.png",
        "friends_unswerving_xlbg@2x.png" : "friends_snowlotus_friends_bg@2x.png",
        "friends_unswerving_xdbg@2x.png" : "friends_heart_friends_bg@2x.png",
        # -------------长方形的-------------
        "friends_ex_qmbg@2x.png" : "friends_closefriends_once_bg@2x.png",
        "friends_ex_cqbg@2x.png" : "friends_longlovefriends_once_bg@2x.png",
        "friends_ex_bybg@2x.png" : "friends_unswerving_once_bg@2x.png",
        "friends_ex_yhbg@2x.png" : "friends_eternal_once_bg@2x.png",
        "friends_ex_tsbg@2x.png" : "friends_angel_once_bg@2x.png",
        "friends_ex_wybg@2x.png" : "friends_only_once_bg@2x.png",
        "friends_ex_ssbg@2x.png" : "friends_sansheng_once_bg@2x.png",
        "friends_ex_fdbg@2x.png" : "friends_girlFriend_once_bg@2x.png",
        "friends_ex_jlbg@2x.png" : "friends_jinlanfriends_once_bg@2x.png",
        "friends_ex_bbbg@2x.png" : "friends_biyifriends_once_bg@2x.png",
        "friends_ex_llbg@2x.png" : "friends_liulijinzhunfriends_once_bg@2x.png",
        "friends_ex_hybg@2x.png" : "friends_huayufriends_once_bg@2x.png",
        "friends_ex_rybg@2x.png" : "friends_sun_moon_stone_friends_once_bg@2x.png",
        "friends_ex_fhbg@2x.png" : "friends_fengqiuhuang_friends_once_bg@2x.png",
        "friends_ex_xybg@2x.png" : "friends_xingyue_friends_once_bg@2x.png",
        "friends_ex_xlbg@2x.png" : "friends_snowlotus_friends_once_bg@2x.png",
        "friends_ex_xdbg@2x.png" : "friends_heart_friends_once_bg@2x.png",
    }
    
    # 源目录
    source_directory = "../sources/new"
    
    # 目标目录
    dest_directory = "../sources/output"
    
    empty_directory(dest_directory)
    # 执行拷贝并重命名操作
    copy_rename_files(file_mapping, source_directory, dest_directory)