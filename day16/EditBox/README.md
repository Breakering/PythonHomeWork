### (1)作业名称：后台管理平台

### (2)作者：赵晋彪

### (3)博客地址：

   <http://www.cnblogs.com/breakering/p/7287231.html>

### (4)作业需求：

1. 非编辑模式：
    可对每行进行选择； 反选； 取消选择
2. 编辑模式:
    进入编辑模式时如果行被选中，则被选中的行万变为可编辑状态，未选中的不改变
    退出编辑模式时，所有的行进入非编辑状态
    处于编辑模式时，行被选中则进入编辑状态，取消选择则进入非编辑状态

### (5)本次作业实现的需求：

1. 非编辑模式：
    可对每行进行选择, 全选, 反选, 取消选择
2. 编辑模式:
    进入编辑模式时如果行被选中，则被选中的行变为可编辑状态，未选中的不改变
    退出编辑模式时，所有的行进入非编辑状态
    处于编辑模式时，行被选中则进入编辑状态，取消选择则进入非编辑状态
    处于编辑模式时，全选则所有行进入编辑状态，取消则所有行进入非编辑状态，反选则是
    之前处于非编辑状态的则会变为编辑状态，反之同理
3. 完成了批量上线下线功能，按住CTRL实现

### (6)测试：

1) 直接打开index.html即可进行测试

### (7)备注：
在处理批量上线时花费了大量时间查找资料，但是都不是太准确，后来请教了导师知道了监控键盘按键的方法才解决了，这里要谢谢刘导，
然后在处理select选择的时候出现了点小问题，设置selected="selected"有时无法显示选中的option，后来尝试用val()来设置才解决了
此问题，而且代码量也减少了，nice。