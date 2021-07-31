import os
command = """ echo 'namespace :katello do
  desc <<-END_DESC 
This is a rake script to fetch and list released packages of satellite. 
This list will be unique based on Which version of Red Hat Satellite is installed.
 

Author: Jaskaran Singh Narula 
IRC: Jaskaran
Github: https://github.com/JaskaranNarula


END_DESC

  task :List_all_released_packages => :environment do
    ary = Katello::Ping.packages.sort
     File.open(\"/tmp/released_packages.txt\", \"w\") do |file|
      ary.each do |i|
      file.puts i
      end
     end
  end
end
'  > /usr/share/foreman/lib/tasks/get_packages_from_satellite.rake """


os.system(command)
os.system("foreman-rake katello:List_all_released_packages") 
os.system("yum list installed > /tmp/yum_list_installed.txt")
file1 = open("/tmp/yum_list_installed.txt", "r")
package_names_from_yum = []
for each in file1:
	y = each.split(" ")[0].split(".")
	if y[0] == '':
		pass
	else:
		package_names_from_yum.append(y[0])
file2 = open("/tmp/released_packages.txt", "r")
released_packages = []
for each in file2:
	a = each.split("-")
	for i in a:
		try:
			if type(int(i[0])) is int:	
				version_index = a.index(i)
				joined_names  = "-".join(a[:version_index])
				released_packages.append(joined_names)
				break
		except:
			pass	
package_names_from_yum = package_names_from_yum[5:]
not_found = []
found     = []
for i in released_packages:
	if i in package_names_from_yum:
		found.append(i) 
	else:
		not_found.append(i)	
print("The packages which are not found as per released packages for Red Hat Satellite 6 ")
for i in not_found:
	print(i) 
