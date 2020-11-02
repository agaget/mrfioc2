from org.csstudio.opibuilder.scriptUtil import PVUtil, ConsoleUtil

table = widget.getTable()

times = PVUtil.getDoubleArray(pvs[0])
codes = PVUtil.getDoubleArray(pvs[1])
mask = PVUtil.getDoubleArray(pvs[2])
ena = PVUtil.getDoubleArray(pvs[3])

N = min(len(times), len(codes),len(mask),len(ena))

while table.getRowCount()<N:
	table.insertRow(table.getRowCount())

while table.getRowCount()>N:
	table.deleteRow(table.getRowCount()-1)

times, codes, mask, ena = times[:N], codes[:N], mask[:N], ena[:N]

for row,(T,C,M,EN) in enumerate(zip(times, codes, mask, ena)):
	table.setCellText(row,0,str(T))
	table.setCellText(row,1,"%d"%C)
	table.setCellText(row,2,"%d"%M)
	table.setCellText(row,3,"%d"%EN)
