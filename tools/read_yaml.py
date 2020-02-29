import yaml
import os


# 编写读取 yaml文件方法


def read_yaml(file_name, key):
    # 1. 获取文件流
    with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r", encoding="utf-8") as f:
        # 2.调用safe_load方法
        case_data = yaml.safe_load(f)[key]
        # 遍历数据 新增空列表
        data_list = list()
        for i in case_data.values():
            data_list.append(i)

        # 返回列表
        return data_list


if __name__ == '__main__':
    print(read_yaml("login.yaml", "test_login"))
