/**
 * @file src/python/ip/src/main.cc 
 * @author <a href="mailto:andre.dos.anjos@cern.ch">Andre Anjos</a> 
 *
 * @brief Combines all modules to make up the complete bindings
 */

#include <boost/python.hpp>

using namespace boost::python;

void bind_ip_ipcore();
void bind_ip_color();
void bind_ip_oldcolor();
void bind_ip_vision();
void bind_ip_image();
void bind_ip_lbp();
void bind_ip_filters();
void bind_ip_filters_new();
void bind_ip_flow();
void bind_ip_dctfeatures();
void bind_ip_geomnorm();
void bind_ip_tantriggs();

BOOST_PYTHON_MODULE(libpytorch_ip) {
  scope().attr("__doc__") = "Torch image processing classes and sub-classes";
  bind_ip_ipcore();
  bind_ip_color();
  bind_ip_oldcolor();
  bind_ip_vision();
  bind_ip_image();
  bind_ip_lbp();
  bind_ip_filters();
  bind_ip_filters_new();
  bind_ip_flow();
  bind_ip_dctfeatures();
  bind_ip_geomnorm();
  bind_ip_tantriggs();
}
