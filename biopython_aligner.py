from Bio.Seq import Seq


my_seq = Seq("ACTGATGACTGCTGA")

print("The sequence %s is %i bases long" % (my_seq, len(my_seq)))
print("reverse complement is %s" % my_seq.reverse_complement())
print("protein translation is %s" % my_seq.translate())