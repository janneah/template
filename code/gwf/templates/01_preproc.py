from gwf import AnonymousTarget

def template_template(inputfile):
	'''
	Template for making a gwf template
	'''
    output_name = modpath(inputfile, path='steps/', suffix='.vcf')

	# Defining inputs, outputs and ressources
	inputs = {'input': inputfile}
	outputs = {'output': output_name}
	options = {
		'memory': '60g',
		'walltime': '00:00:00',
		'cores': 'cores',
		'account': 'account'
	}
	
	# Command to be run in the terminal
	spec = f'''
	
    some command {inputfile} {output_name}
	
	'''

	return AnonymousTarget(inputs=inputs, outputs=outputs, options=options, spec=spec)

def naming_template(idx, target):

    job_name = modpath(target.inputs['input'], parent='', suffix='')

    return f'template_{job_name}'
