import time
from selenium import webdriver

element_list = []
idx = 0


def tree2(node, depth, max_depth, show_text):
    global element_list
    global idx

    if max_depth != -1 and depth > max_depth:
        return

    print(' '*depth*2, '', node.tag_name, '[', idx, '] ', sep='', end='')
    if show_text:
        print(repr(node.text[:20]), sep='', end='')
    print()

    element_list.append(node)
    idx += 1

    print('c1')

    sub_nodes = node.find_elements_by_xpath("child::*")
    print('c2')
    if not sub_nodes:
        return
    for nd in sub_nodes:
        tree2(nd, depth+1, max_depth, show_text)


def tree(node, max_depth=-1, show_text=False):
    global element_list
    global idx
    element_list = []
    idx = 0

    tree2(node, 0, max_depth, show_text)


def select_node(idx):
    return element_list[idx]
