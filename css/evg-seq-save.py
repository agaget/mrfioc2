from org.csstudio.opibuilder.scriptUtil import PVUtil, ConsoleUtil
from jarray import array

Timestamp_SP = pvs[0]
EvtCode_SP = pvs[1]
Mask_SP = pvs[2]
Ena_SP = pvs[3]

T, E, M, EN = [], [], [], []
for row in widget.getTable().getContent():
	T.append(float(row[0]))
	ConsoleUtil.writeInfo("test 1 "+str(row[0]))
	E.append(float(row[1]))
	ConsoleUtil.writeInfo("test 2 "+str(row[1]))
	M.append(float(row[2]))
	ConsoleUtil.writeInfo("test 3 "+str(row[2]))
	EN.append(float(row[3]))
	ConsoleUtil.writeInfo("test 4 "+str(row[3]))



Timestamp_SP.setValue(array(T, 'd'))
EvtCode_SP.setValue(array(E, 'd'))
Mask_SP.setValue(array(M, 'd'))
Ena_SP.setValue(array(EN, 'd'))
