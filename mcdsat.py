import query_rewriting
import mcdsat

class mcdsat(query_rewriting.Query_Rewriting):
	"""
	Child class which implements the MCDSAT algorithm for Query Rewriting and MCDs Genreration
	URL to the parent class - 
	"""	

	def __init__(self):
		"""
		Task -- Initialize the algorithm specific data memebers using this constructor

		self.algorithm is set to mcdsat
		self.c2d_path -- string -- path to the c2d compiler executable
		self.models -- string -- path to the dnnf models folder
		self.cnf_file -- string -- path to the file which stores the intermediate result of this algorith, ie a CNF file
		self.compiled_cnf -- string -- path to the file containing the compiled dnnf models
		self.query_models -- string -- path to the file containing all the generated query models using MCDSAT
		"""
		self.algorithm = "mcdsat"
		self.c2d_path = ""
		self.models = ""
		self.cnf_file = ""
		self.compiled_dnnf = ""
		self.query_models = ""
		
	def read_input(self, query="examples/query.txt", views="examples/views.txt"):
		"""
		Abstract Function Implementation
		Task - Reads the query and view files and stores their path in class members. Saves the c2d compiler and models path if specified
			   Also sets the algorithm that the calling object will be using for Query Rewriting or MCDs generation	

		Input:
		self -- mcdsat object calling this function
		query -- string -- directory path to the queries file
		views -- string -- directory path to the views file

		Result:
		Stores the values of the above input values into the class members   
		"""
		pass

	def generate_query_rewritings(self, c2d_path="c2d/c2d_linux", models="dnnf_models/models/" output_file="results/rewriting.txt"):
		"""
		Abstract Function Implementation
		Task -- Genrate Query Rewritings using the input given input using the MCDSAT algorithm

		Input:
		self -- mcdsat object calling this function
		c2d_path -- string -- directory path to the off-the-shelf c2d compiler
		models -- string -- directory path to off-the-shelf models folder
		output_path -- string -- directory path to the resulting query rewritings

		Result:
		Generates query rewritings and writes to the specified output_file path
		Sets self.rw_flag to True
		Sets the self.generated_rewritings to point to the output_file path
		"""
		pass

	def convertToCNF(self, output_file):
		"""
		Task -- Convert the query into CNF and store it in a .cnf file

		Input:
		self -- mcdsat object calling this function
		output_file -- string -- directory path to save the generated CNF model from the original queries

		Return:
		Stores the CNF model into the output_file
		Sets the self.cnf_file to the output_file

		"""
		pass

	def compileToDNNF(self, cnf_file, output_file):
		"""
		Task -- Compiles the generated CNF into DNNF using the c2d compiler

		Input:
		self -- mcdsat object calling this function
		cnf_file -- string -- (default self.cnf_file) Path containing the cnf model of the input queries
		output_file -- directory path to store the compiled dnnf models

		Result:
		Resulting dnnf models in output_file
		Sets the self.compiled_dnnf_file to output_file
	
		"""
		pass

	def generateModels(self, cnf_file=self.cnf_file, dnnf_file=self.compiled_dnnf_file, output_file):
		"""
		Task -- Generated all models for the given input query using the cnf_file, dnnf_file and the dnnf models

		Input:
		self -- mcdsat object calling this function
		cnf_file -- string -- (default self.cnf_file) Path containing the cnf model of the input queries
		dnnf_file -- string -- (default self.compiled_dnnf_file) Path containing the compiled dnnf models
		output_file -- string -- directory path to store all the generated models

		Result:
		All the resulting models are stored in output_file
		Sets the self.query_models to point to this output_file
		"""
		pass
	
	def generate_MCDs(self, c2d_path="c2d/c2d_linux", models="dnnf_models/models/" output_file="results/rewriting.txt"):
		"""
		Abstract Function Implementation
		Task -- Genrate MCDs using the input given input using the MCDSAT algorithm

		Input:
		self -- mcdsat object calling this function
		c2d_path -- string -- directory path to the off-the-shelf c2d compiler
		models -- string -- directory path to off-the-shelf models folder
		output_path -- string -- directory path to the resulting generated MCDs

		Result:
		Generates query rewritings and writes to the specified output_file path
		Sets self.mcd_flag to True
		Sets self.query_mcds to point to the output_file path
		"""
		pass

if __name__ == '__main__':
	mcdsat = mcdsat()
