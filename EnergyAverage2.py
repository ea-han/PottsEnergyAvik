import os
import pdb
import json

class EnergyAverage2:
    seqStack = []
    consensus = []
    jFileArray = []
    reduxName = ""
    mutationList = []

    
    INTERACTION1 = "Rescue"
    INTERACTION2 = "Compensatory"
    INTERACTION3 = "Antagonistic"

    ##search list of sequences for mutations 1 and 2
    ##add found mutations to a list of sequences to calculate energy of
    ##reduce sequences and mutations with redux file
    ##calculate average of all sequences
    ##mutations: [index, source, [mut1, mut2,etc]],[index2, source2, [mut1, mut2,etc]],

    def __init__(self,seqStack, consensus, mutationList, jFileArray, reduxName):
        self.foundSeqs = []
        self.seqStack = seqStack
        self.reduxName = reduxName
        self.jFileArray = jFileArray
        self.consensus = self.reduceSequence(consensus)
        self.mutationList = mutationList

    def arrToString(self,mutation):
        altMutations = '/'.join(mutation[2])
        newString = ''
        newString = newString + str(mutation[1])
        newString = newString + str(mutation[0]+1)
        newString = newString + altMutations
        return newString

    ##  reduces sequence stack to json file
    def preReduceToJson(self):
        newFullStack = []
        for seq in self.seqStack:
            newFullStack.append(self.reduceSequence(seq))
            with open("reduced.in.fullseq.json", "w") as outfile:
                json.dump(newFullStack, outfile)

    ##loads stack from json file
    def loadJson(self):
        with open("out/reduced.in.fullseq.json") as inputFile:
            self.seqStack = json.load(inputFile)

    def reduceAllMutations(self):
        for mutPair in self.mutationList:
            mutPair = self.reduceMutations(mutPair)
        #breakpoint()

    ## reduces mutations
    def reduceMutations(self,mutationPair): 
        ctr = 0
        mutation1 = mutationPair[0]
        mutation2 = mutationPair[1]
        with open(self.reduxName) as kFile:
            for line in kFile:
                if ctr == mutation1[0]:
                    line = line.strip()
                    insertArr = line.split()
                    aAlpha = list(insertArr[1])
                    bAlpha = list(insertArr[2])
                    cAlpha = list(insertArr[3])
                    dAlpha = list(insertArr[4])
                    
                    val1 = mutation1[1]
                    val2 = mutation1[2][0]
                    if val1 in aAlpha:
                        mutation1[1] = 'A'
                    elif val1 in bAlpha:
                        mutation1[1] = 'B'
                    elif val1 in cAlpha:
                        mutation1[1] = 'C'
                    elif val1 in dAlpha:
                        mutation1[1] = 'D'
                    else:
                        print("invalid mutation: " + mutation1)
                        return -1
                    
                    if val2 in aAlpha:
                        mutation1[2] = 'A'
                    elif val2 in bAlpha:
                        mutation1[2] = 'B'
                    elif val2 in cAlpha:
                        mutation1[2] = 'C'
                    elif val2 in dAlpha:
                        mutation1[2] = 'D'
                    else:
                        print("invalid mutation: " + mutation1)
                        return -1
                    
                    
                    
                elif ctr == mutation2[0]:
                    line = line.strip()
                    insertArr = line.split()
                    aAlpha = list(insertArr[1])
                    bAlpha = list(insertArr[2])
                    cAlpha = list(insertArr[3])
                    dAlpha = list(insertArr[4])
                    
                    val1 = mutation2[1]
                    val2 = mutation2[2][0]
                    if val1 in aAlpha:
                        mutation2[1] = 'A'
                    elif val1 in bAlpha:
                        mutation2[1] = 'B'
                    elif val1 in cAlpha:
                        mutation2[1] = 'C'
                    elif val1 in dAlpha:
                        mutation2[1] = 'D'
                    else:
                        print("invalid mutation: " + mutation2)
                        return -1
                    
                    if val2 in aAlpha:
                        mutation2[2] = 'A'
                    elif val2 in bAlpha:
                        mutation2[2] = 'B'
                    elif val2 in cAlpha:
                        mutation2[2] = 'C'
                    elif val2 in dAlpha:
                        mutation2[2] = 'D'
                    else:
                        print("invalid mutation: " + mutation2)
                        return -1
                ctr += 1

            
        
        return [mutation1,mutation2]
    
    ##reduces sequences
    def reduceSequence(self, seq):
        ctr = 0
        with open(self.reduxName) as kFile:
                returnSeq = []
                for line in kFile:
                    ##simlify
                    line = line.strip()
                    insertArr = line.split()
                    ctr = int(insertArr[0])
                    aAlpha = list(insertArr[1])
                    bAlpha = list(insertArr[2])
                    cAlpha = list(insertArr[3])
                    dAlpha = list(insertArr[4])
                    
                    val = seq[ctr]
                    if val in aAlpha:
                        returnSeq.append('A')
                    elif val in bAlpha:
                        returnSeq.append('B')
                    elif val in cAlpha:
                        returnSeq.append('C')
                    elif val in dAlpha:
                        returnSeq.append('D')
                    else:
                        print("`invalid char`:",val ,flush=True)
                        return -1
                    ctr+=1
        return returnSeq

    def reduceStack(self):
        for i in range(0, len(self.seqStack)):
            self.seqStack[i] = self.reduceSequence(self.seqStack[i])

        
    def getCoupling(self, iVal,jVal):
        aVali = ord(iVal) - 65
        aValj = ord(jVal) - 65
        if (aVali < 0 or aVali > 3):
            print("invalid coupling")
            return
        if (aVali == 0 and aValj == 0):
            return 0
        if (aVali == 0 and aValj == 1):
            return 1
        if (aVali == 0 and aValj == 2):
            return 2
        if (aVali == 0 and aValj == 3):
            return 3
        if (aVali == 1 and aValj == 0):
            return 4
        if (aVali == 1 and aValj == 1):
            return 5
        if (aVali == 1 and aValj == 2):
            return 6
        if (aVali == 1 and aValj == 3):
            return 7
        if (aVali == 2 and aValj == 0):
            return 8
        if (aVali == 2 and aValj == 1):
            return 9
        if (aVali == 2 and aValj == 2):
            return 10
        if (aVali == 2 and aValj == 3):
            return 11
        if (aVali == 3 and aValj == 0):
            return 12
        if (aVali == 3 and aValj == 1):
            return 13
        if (aVali == 3 and aValj == 2):
            return 14
        if (aVali == 3 and aValj == 3):
            return 15
        return -1

    ##gets energy of a sequence
    def getEnergy(self, seq):
        ctr = 0
        energy = 0
        length = len(seq)

        for i in range(0,length):
            iAcid = seq[i]
            for j in range (i+1,length):
                jAcid = seq[j]
                couplingIdx = self.getCoupling(iAcid,jAcid)
                if couplingIdx < 0:
                    print("coupling failed")
                    return -1
                energy += self.jFileArray[ctr][couplingIdx]
                ctr+=1
        return energy

    def mutateSequence1Consensus(self, seq,mutation):
        sequence = list(seq)
        sequence[mutation[0]] = mutation[2]
        return sequence
    
    def mutateSequence2Consensus(self, seq,mutation1,mutation2):
        sequence = list(seq)
        sequence[mutation1[0]] = mutation1[2]
        sequence[mutation2[0]] = mutation2[2]
        return sequence
    
    ##takes reduced sequence andmutation and calcultes energies. Need to screen for valid mutation/sequences.
    #runs? need to check avlues
    def calcEnergySequence(self,seq,name,mutationArray):
        
        defaultEnergy = self.getEnergy(seq) ##works
        m1Energy = self.getEnergy(self.mutateSequence1Consensus(seq, mutationArray[0]))
        m2Energy = self.getEnergy(self.mutateSequence1Consensus(seq, mutationArray[1]))
        m1m2Energy = self.getEnergy(self.mutateSequence2Consensus(seq,mutationArray[0],mutationArray[1])) ##works

        m1Delta = defaultEnergy - m1Energy 
        m2Delta = defaultEnergy - m2Energy
        m1m2Delta = defaultEnergy - m1m2Energy 
        deltaDeltaE = m1m2Delta - (m1Delta + m2Delta)

        return [mutationArray,name,deltaDeltaE,m1m2Delta,m1Delta,m2Delta]
    
    ##computes all the sequence values for a given mutation
    ##TODO rewrite in C and call cdef from cython
    ##      -checkIfEligible, calcEnergySequence
    def computeSeqsForMutation(self,mutationPair):
        outputArr = []
        ##mutationpair, seq index, delta delta, d12, d1, d2
        index = 0
        for seq in self.seqStack:
            if self.checkIfEligible(seq, mutationPair) == True:
                outputArr.append(self.calcEnergySequence(seq,index,mutationPair))
            index+=1
        ##breakpoint() ##computed 1 seqstack
        return outputArr


    ##for each mutation in mutationlist, compute all values. return list of lists of values
    def computeValueStacks(self):
        ##reduces stack NOTE: now using imported json file
        ##self.reduceStack()

        ##output Format: [[mutation,computed stack values],[mutation,computed stack values]]
        computedArr = []
        outputArr = []

        #this runs
        for mutPair in self.mutationList:
            computedArr = self.computeSeqsForMutation(mutPair)
            ##add stack to outputarr
            outputArr.append([mutPair,computedArr])
            ##breakpoint() ##computed 1 mutpair stack
        #breakpoint()

        with open("out/valueStack.json", "w") as outfile1:
            json.dump(outputArr, outfile1)        
        return outputArr

    ##works on consensus?
    def checkIfEligible(self, seq, mutPair):
        mut1 = mutPair[0]
        mut2 = mutPair[1]
        index1 = mut1[0]
        index2 = mut2[0]
        preMut1 = mut1[1]
        preMut2 = mut2[1]

        if seq[index1] == preMut1 and seq[index2] == preMut2:
            return True
        else:
            return False



    ##takes in SINGLE MUTATION valuestack,compares each sequence DDE with consensus and classifies.
    ##Sorts and returns all values in valuestack
    ##returns []
    def getInteractionsAndDifference(self,mutationData):
        mutPair = mutationData[0]
        valueStack = mutationData[1]

        rescue = []
        compensate = []
        antag = []

        ##pdb.set_trace()

        #get consensus interaction
        consensusData = self.calcEnergySequence(self.consensus,"consensus", mutPair)
        consensusInteraction = self.getInteraction(consensusData[4],consensusData[5],consensusData[3])
        print(consensusData, consensusInteraction)

        index = 0
        for seqArr in valueStack:
            actualDeltam1m2 = seqArr[3]
            distFromMaxDelta1 = actualDeltam1m2 - max(seqArr[4],seqArr[5])

            ##check interaction
            interaction = self.getInteraction(seqArr[4], seqArr[5], actualDeltam1m2)
            seqData = [mutPair,index,interaction,distFromMaxDelta1,actualDeltam1m2]
            index+=1
            if interaction == self.INTERACTION1:
                rescue.append(seqData)
            elif interaction == self.INTERACTION2:
                compensate.append(seqData)
            else:
                antag.append(seqData)
        
        return [rescue,compensate,antag]

    
    def importValueStacks(self,valueStack):
        with open("src/valueStack.json") as oFile:
            returnArr = json.load(oFile)
        return returnArr
        

    #returns interaction
    def getInteraction(self,Dm1,Dm2, actual):
        projectedDelta = Dm1 + Dm2
        if actual < projectedDelta:
            return self.INTERACTION3
        elif actual > max(Dm1,Dm2):
            return self.INTERACTION1
        else:
            return self.INTERACTION2
    
    #sort function for compareToConsensus
    def sortFunc1(e):
        return e[2]


    ##compares value stack interactions with consensus. sorts into one big list by interaction, delta difference.
    ##combine all relevant data into one entry. 
    ## label,index,interaction,consensusInteraction,deltaDifference
    ##returns 2 arrays:[same as consensus, diff to consensus]
    def compareToConsensus(self):
        ##gets values: [[mutation,computed stack values],[mutation,computed stack values],...]
        sequenceCalculations = self.computeValueStacks()

        #breakpoint() ##computed value stacks

            ##sequenceCalulations: [[mutation,computed stack values],[mutation,computed stack values]]
        for mutationData in sequenceCalculations:
            appendArr = self.getInteractionsAndDifference(mutationData)
            mutName = self.arrToString(mutationData[0][0]) + "-" + self.arrToString(mutationData[0][1])
            print(mutName)
            seqData = self.getInteractionsAndDifference(mutationData)
            rescue = seqData[0]
            compensate = seqData[1]
            antag = seqData[2]
            
            with open("out/"+mutName+".rescue.json", "w") as outfile1:
                json.dump(rescue, outfile1)
            with open("out/"+mutName+".compensate.json", "w") as outfile2:
                json.dump(compensate, outfile2)
            with open("out/"+mutName+".antag.json", "w") as outfile3:
                json.dump(antag, outfile3)


        
        
        #sameAsConsensus.sort(key=self.sortFunc1)
        #diffToConsensus.sort(key=self.sortFunc1)
        
        

##TODO: add mutation screen for fullseq, sort based on delta difference, combine relevant data, finish compare to consensus, test
            


    
    


        










        

        