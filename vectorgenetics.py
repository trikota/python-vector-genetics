import inspect, random, sys
import numpy as np
import matplotlib.pyplot as plt

class VectorEvolution:
    def __init__(self, evaluator, vector_shape):
        self.evaluator = evaluator #function that measures performance error
        self.vector_shape = vector_shape #size of creature
       
    #main method
    def evolve(self, population=100, generations=300, split_size=0.2, mutation_rate=0.15, plot_gen_best=False, plot_best=True):
        creatures = np.random.random((population,)+self.vector_shape) #starting population
        for generation in range(generations):
            results = [] #performance error of all each creature
            for i,creature in enumerate(creatures):
                results.append({'val':self.evaluate(creature), 'i':i})
            #sort to select best of them. lets call them x-partners
            sorted_results = sorted(results, key=lambda k: k['val']) 
            best = []
            for _ in range(int(split_size*population)):
                best.append(creatures[sorted_results[_]['i']])
            #randomly chosen y partners (of all population including best ones)
            casual = [ creatures[i] for i in random.sample(xrange(population), int((1-split_size)*population)) ]
            offsprings = []
            for y in casual: #for each y partner
                #randomly chosen x partner
                partner_i = random.randint(0,len(best)-1)
                partner = best[partner_i]
                #produce an offspring
                offspring = self.fuse(y, partner, mutation_rate)
                offsprings.append(offspring)
            #all "not so good" y parents die
            #only the "best ones" and newborn children remain alive
            creatures = np.asarray(offsprings+best)
            #print out result so far
            sys.stdout.write("Gen:{}  Best creature:{}\r".format(generation,sorted_results[0]['val']))
            sys.stdout.flush()
            #plot best creature so far on each generation
            if plot_gen_best:
                best_creature = creatures[sorted_results[0]['i']]
                self.plot_creature(best_creature, generation)
        if plot_best: #plot final best creature
            best_creature = creatures[sorted_results[0]['i']]
            self.plot_creature(best_creature, generation)
    
    #function to produce child
    #"dad" is who better performs.
    def fuse(self, mum, dad, mutation_rate):
        #randomly select mum's genes to fuse with dad's. the rest we just keep as they were.
        exchanges = random.sample(xrange(len(dad)), random.randint(0,len(dad)))
        offspring = []
        for i,gene in enumerate(dad):
            if i in exchanges:
                offspring_gene = (mum[i]+dad[i])/2
            else:
                offspring_gene = dad[i]
            #roll a dice
            mutation_prob = random.uniform(0, 1)
            if mutation_prob < mutation_rate:
                #mutate gene a little. 30 is arbitrary
                offspring_gene += (np.random.random(dad[i].shape))/30
            offspring.append(offspring_gene)
        offspring = np.asarray(offspring)
        return offspring
    
    #optional method
    def plot_creature(self,creature,generation):
        x = creature[:,0]
        y = creature[:,1]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        scat = ax.scatter(x, y)
        plt.show() #show plot 
        #also save plot image into folder
        fig.savefig('result_generation_{}.png'.format(generation))
        plt.close(fig) 
    
    def evaluate(self, x):
        #couple of checks before we measure performance
        if type(x) is not tuple:
            x = (x,)
        f_args = inspect.getargspec(self.evaluator)
        try:
            assert len(x) == len(f_args.args)
        except AssertionError as e:
            e.args += ('Wrong number of arguments passed',)
            raise
        return self.evaluator(*x)