# python3
import sys
from collections import defaultdict
 
class Node:
    def __init__(self,state_num,ch=None):
        self.state_num = state_num
        self.ch = ch
        self.children = []
 
class Trie(Node):
    """
    实现了一个简单的字典树
    """
    def __init__(self):
        Node.__init__(self,0)
 
    def init(self):
        self._state_num_max = 0
        self.goto_dic = defaultdict(lambda :-1)
        self.fail_dic = defaultdict(int)
        self.output_dic = defaultdict(list)
 
    def build(self,patterns):
        """
        参数 patterns 如['he', 'she', 'his', 'hers']
        """
        for pattern in patterns:
            self._build_for_each_pattern(pattern)
        self._build_fail()
        
    def _build_for_each_pattern(self,pattern):
        """
        将pattern添加到当前的字典树中
        """
        current = self
        for ch in pattern:
            # 判断字符 ch 是否为节点 current 的子节点
            index = self._ch_exist_in_node_children(current,ch)
            # 不存在 添加新节点并转向
            if index == -1: 
                current = self._add_child_and_goto(current,ch)
            # 存在 直接 goto
            else: 
                current = current.children[index]
        self.output_dic[current.state_num] = [pattern]
 
    def _ch_exist_in_node_children(self,current,ch):
        """
        判断字符 ch 是否为节点 current 的子节点，如果是则返回位置，否则返回-1
        """
        for index in range(len(current.children)):
            child = current.children[index]
            if child.ch == ch:
                return index
        return -1
 
    def _add_child_and_goto(self,current,ch):
        """
        在当前的字典树中添加新节点并转向
        新节点的编号为 当前最大状态编号+1
        """
        self._state_num_max += 1
        next_node = Node(self._state_num_max,ch)
        current.children.append(next_node)
        # 修改转向函数
        self.goto_dic[(current.state_num,ch)] = self._state_num_max
        return  next_node
 
    def _build_fail(self):
        node_at_level = self.children
        while node_at_level:
            node_at_next_level = []
            for parent in node_at_level:
                node_at_next_level.extend(parent.children)
                for child in parent.children:
                    v = self.fail_dic[parent.state_num]
                    while self.goto_dic[(v,child.ch)] == -1 and v != 0:
                        v = self.fail_dic[v]
                    fail_value = self.goto_dic[(v,child.ch)]
                    self.fail_dic[child.state_num] = fail_value
                    if self.fail_dic[child.state_num] != 0:
                        self.output_dic[child.state_num].extend(self.output_dic[fail_value])
            node_at_level = node_at_next_level
 
class AC(Trie):
    def __init__(self):
        Trie.__init__(self)
 
    def init(self,patterns):
        Trie.init(self)
        self.build(patterns)
 
    def goto(self,s,ch):
        if s == 0:
            if (s,ch) not in self.goto_dic:
                return 0
        return self.goto_dic[(s,ch)]
 
    def fail(self,s):
        return self.fail_dic[s]
 
    def output(self,s):
        return self.output_dic[s]
 
    def search(self,text):
        """
        在text中查找字典树中字符串长度最长的词，该最长的词可能不止一个
        """
        current_state = 0
        ch_index = 0
        result_set = set()
        while ch_index < len(text):
            ch = text[ch_index]
            if self.goto(current_state,ch) == -1:
                current_state = self.fail(current_state)
            current_state = self.goto(current_state,ch)
            patterns = self.output(current_state)
            if patterns:    
#                print (current_state,*patterns)
                result_set.add(*patterns)
            ch_index += 1
        max_length_string = ""
        max_length = 0
        max_length_result = []
        for pattern in result_set:
            if len(pattern) >= max_length:
                max_length_string = pattern
                max_length = len(pattern)
                max_length_result.append(pattern)
        print(max_length_result)

    def has_pattern(self,text):
        """
        如果text中存在字典树中的任一一个词，那么就返回True
        """
        current_state = 0
        ch_index = 0
        result_set = set()
        while ch_index < len(text):
            ch = text[ch_index]
            if self.goto(current_state,ch) == -1:
                current_state = self.fail(current_state)
            current_state = self.goto(current_state,ch)
            patterns = self.output(current_state)
            if patterns:    
                return True
            ch_index += 1
        return False


if __name__ == "__main__":
    ac = AC()
    ac.init(['做爱', '性感'])
#    ac.search("ithisherti")
    for line in sys.stdin:
        line = line.strip()
        if ac.has_pattern(line):
            print(line)
