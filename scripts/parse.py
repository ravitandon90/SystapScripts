import fileinput
thread_file = open("/home/tandon/data/threads.txt")
iowait_per_fault = open("/home/tandon/systap/data/iowait_per_fault.txt", "w")
iowait_ave = open("/home/tandon/systap/data/iowait_ave.txt", "w")
fault_ave = open("/home/tandon/systap/data/fault_ave.txt", "w")
runtime_ave = open("/home/tandon/systap/data/runtime_ave.txt", "w")

iowait_per_fault.write("ThreadType::VM,VMGC,CGC,Java\n")
iowait_ave.write("VM,CGC,PGC,Java\n")
runtime_ave.write("VM,CGC,PGC,Java\n")
fault_ave.write("VM,CGC,PGC,Java\n")

vmT=[]
vmgcT=[]
cgcT=[]
javaT=[]

count=0
threadId=0
for line in thread_file:
    ar = line.split(',')
    if count == 0:
       for tid in ar:
          vmT.append(tid.strip(' \t\n\r'))
    elif count == 1:
       for tid in ar:
          cgcT.append(tid.strip(' \t\n\r'))
    elif count == 2:
       for tid in ar:
          vmgcT.append(tid.strip(' \t\n\r'))
    elif count == 3:
       for tid in ar:
          javaT.append(tid.strip(' \t\n\r'))
    count = count + 1

lineCount=0

vmTIOWait=[]
vmgcTIOWait=[]
cgcTIOWait=[]
javaTIOWait=[]

vmTFaults=[]
vmgcTFaults=[]
cgcTFaults=[]
javaTFaults=[]

vmTFaultsMark=0
vmgcTFaultsMark=0
cgcTFaultsMark=0
javaTFaultsMark=0

vmTFaultsTotal=0
vmgcTFaultsTotal=0
cgcTFaultsTotal=0
javaTFaultsTotal=0

vmTIOWaitPerFault=[]
vmgcTIOWaitPerFault=[]
cgcTIOWaitPerFault=[]
javaTIOWaitPerFault=[]

vmTRuntime=[]
vmgcTRuntime=[]
cgcTRuntime=[]
javaTRuntime=[]

vmTRuntimeTotal=0
vmgcTRuntimeTotal=0
cgcTRuntimeTotal=0
javaTRuntimeTotal=0

vmTIOWaitPerFaultTotal=[]
vmgcTIOWaitPerFaultTotal=[]
cgcTIOWaitPerFaultTotal=[]
javaTIOWaitPerFaultTotal=[]

def init():
  vmTIOWait=[]
  vmgcTIOWait=[]
  cgcTIOWait=[]
  javaTIOWait=[] 
  
  vmTFaults=[]
  vmgcTFaults=[]
  cgcTFaults=[]
  javaTFaults=[]

  vmTIOWaitPerFault=[]
  vmgcTIOWaitPerFault=[]
  cgcTIOWaitPerFault=[]
  javaTIOWaitPerFault=[]

  return



def average(array):
   sum = 0
   n_sum = 0
   for num in array: 
     sum = sum + num
     n_sum = n_sum + 1
   if n_sum == 0:
     return 0
   return sum/n_sum

def print_runtime_ave():
    ave = average(vmTRuntime)
    runtime_ave.write(str(ave)+',')     
    ave = average(vmgcTRuntime)
    runtime_ave.write(str(ave)+',')     
    ave = average(cgcTRuntime)
    runtime_ave.write(str(ave)+',')     
    ave = average(javaTRuntime)
    runtime_ave.write(str(ave)+'\n')     
    return  

def print_iowait_ave():
    ave = average(vmTIOWait)
    iowait_ave.write(str(ave)+',')     
    ave = average(vmgcTIOWait)
    iowait_ave.write(str(ave)+',')     
    ave = average(cgcTIOWait)
    iowait_ave.write(str(ave)+',')     
    ave = average(javaTIOWait)
    iowait_ave.write(str(ave)+'\n')     
    return  

def print_iowait_per_fault():
    iowait_per_fault.write("IOWait Per Fault Mark Phase:")
    ave = average(vmTIOWaitPerFault)
    iowait_per_fault.write(str(float(ave)/1000)+'ms,')     
    ave = average(vmgcTIOWaitPerFault)
    iowait_per_fault.write(str(float(ave)/1000)+'ms,')     
    ave = average(cgcTIOWaitPerFault)
    iowait_per_fault.write(str(float(ave)/1000)+'ms,')     
    ave = average(javaTIOWaitPerFault)
    iowait_per_fault.write(str(float(ave)/1000)+'ms\n')     
    return

def print_ave_faults():
    ave = average(vmTFaults)
    fault_ave.write(str(ave)+',')     
    ave = average(vmgcTFaults)
    fault_ave.write(str(ave)+',')     
    ave = average(cgcTFaults)
    fault_ave.write(str(ave)+',')     
    ave = average(javaTFaults)
    fault_ave.write(str(ave)+'\n')  
    return

def print_iowait_per_fault_total():
    iowait_per_fault.write("IOWait Per Fault Total:")
    ave = average(vmTIOWaitPerFaultTotal)
    iowait_per_fault.write(str(float(ave)/1000)+'ms,')
    ave = average(vmgcTIOWaitPerFaultTotal)
    iowait_per_fault.write(str(float(ave)/1000)+'ms,')
    ave = average(cgcTIOWaitPerFaultTotal)
    iowait_per_fault.write(str(float(ave)/1000)+'ms,')
    ave = average(javaTIOWaitPerFaultTotal)
    iowait_per_fault.write(str(float(ave)/1000)+'ms\n')
    return

def print_total_faults():
    iowait_per_fault.write("Total Faults:")
    iowait_per_fault.write(str(vmTFaultsTotal/1000)+'K,')
    iowait_per_fault.write(str(vmgcTFaultsTotal/1000)+'K,')
    iowait_per_fault.write(str(cgcTFaultsTotal/1000)+'K,')
    iowait_per_fault.write(str(javaTFaultsTotal/1000)+'K\n')    
    return 

def print_mark_phase_faults():
    iowait_per_fault.write("Mark Phase Faults:")
    iowait_per_fault.write(str(sum(vmTFaults))+',')
    iowait_per_fault.write(str(sum(vmgcTFaults))+',')
    iowait_per_fault.write(str(sum(cgcTFaults))+',')
    iowait_per_fault.write(str(sum(javaTFaults))+'\n')    
    return 

def print_runtime_total():
    iowait_per_fault.write("Total Runtime:")
    iowait_per_fault.write(str(vmTRuntimeTotal/1000000)+'s,')
    iowait_per_fault.write(str(vmgcTRuntimeTotal/1000000)+'s,')
    iowait_per_fault.write(str(cgcTRuntimeTotal/1000000)+'s,')
    iowait_per_fault.write(str(javaTRuntimeTotal/1000000)+'s\n')
    return

def print_stats():
    print_iowait_per_fault()
    print_iowait_per_fault_total()
    print_total_faults()
    print_runtime_total()
    print_mark_phase_faults()
    #print_ave_faults()
    #print_iowait_ave()
    #print_runtime_ave()
    return

init()
phase = 0
for line in fileinput.input():
    if(line == "vm_exit\n"):
      phase = 1
      continue
    if(phase == 1):
      sp_array = line.split()
      threadId = sp_array[0] 
      if threadId in vmT:  
        vmTFaultsTotal = vmTFaultsTotal + int(sp_array[2])
        vmTRuntimeTotal = vmTRuntimeTotal + int(sp_array[3])
        if(int(sp_array[2]) > 0):
          vmTIOWaitPerFaultTotal.append(int(sp_array[1])/int(sp_array[2]))
      elif threadId in vmgcT:
        vmgcTFaultsTotal = vmgcTFaultsTotal + int(sp_array[2])
        vmgcTRuntimeTotal = vmgcTRuntimeTotal + int(sp_array[3])
        if(int(sp_array[2]) > 0):
          vmgcTIOWaitPerFaultTotal.append(int(sp_array[1])/int(sp_array[2]))
      elif threadId in cgcT:
        cgcTFaultsTotal = cgcTFaultsTotal + int(sp_array[2])
        cgcTRuntimeTotal = cgcTRuntimeTotal + int(sp_array[3])
        if(int(sp_array[2]) > 0):
          cgcTIOWaitPerFaultTotal.append(int(sp_array[1])/int(sp_array[2]))
      elif threadId in javaT:
        javaTFaultsTotal = javaTFaultsTotal + int(sp_array[2])
        javaTRuntimeTotal = javaTRuntimeTotal + int(sp_array[3])
        if(int(sp_array[2]) > 0):
          javaTIOWaitPerFaultTotal.append(int(sp_array[1])/int(sp_array[2]))
      continue
  
    if(line == "mark_from_roots_end\n"):
      continue
    sp_array = line.split()
    threadId = sp_array[0]
    if threadId in vmT:
       vmTIOWait.append(int(sp_array[1]))
       vmTFaults.append(int(sp_array[2]))
       #vmTRuntime.append(int(sp_array[2]))
       if(int(sp_array[2]) > 0):
          vmTIOWaitPerFault.append(int(sp_array[1])/int(sp_array[2]))
          #print float(int(sp_array[1])/int(sp_array[2]))/1000

    elif threadId in vmgcT:
       vmgcTIOWait.append(int(sp_array[1]))
       vmgcTFaults.append(int(sp_array[2]))
       #vmgcTRuntime.append(int(sp_array[2]))
       if(int(sp_array[2]) > 0):
         vmgcTIOWaitPerFault.append(int(sp_array[1])/int(sp_array[2]))
         print float(int(sp_array[1])/int(sp_array[2]))/1000

    elif threadId in cgcT:
      cgcTIOWait.append(int(sp_array[1])) 
      cgcTFaults.append(int(sp_array[2]))
      #cgcTRuntime.append(int(sp_array[2]))
      if(int(sp_array[2]) > 0):
          cgcTIOWaitPerFault.append(int(sp_array[1])/int(sp_array[2]))
          #print float(int(sp_array[1])/int(sp_array[2]))/1000

    elif threadId in javaT:  
      javaTIOWait.append(int(sp_array[1]))
      javaTFaults.append(int(sp_array[2]))
      #javaTRuntime.append(int(sp_array[2]))
      if(int(sp_array[2]) > 0):
          javaTIOWaitPerFault.append(int(sp_array[1])/int(sp_array[2]))
          #print float(int(sp_array[1])/int(sp_array[2]))/1000
     
    lineCount = lineCount + 1
    
print_stats()
iowait_per_fault.close()
iowait_ave.close()
fault_ave.close()
runtime_ave.close()
fileinput.close()
