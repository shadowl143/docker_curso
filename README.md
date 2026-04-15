# docker_curso
Curso intermedio de docker


# Configuración.
solo colocate en la raiz del proyecto y en seguida ejecuta docker-compose -p <nombreimagen> up -d


#Precacion.
1. el docker file tienen una linea de ports: en db la sintqaxis es algo asi como
   *  ports:
      <b>- "3306":"3306"</b>
    esa linea fue eliminada ya que si tienes una base de datos expuesta por ese puerto no te va a funcionar si quieres exponeral y ya esta en uso ese puerto es necesario hacer el cambio
   * ports:
     <b>- <puertomaquina>:"3306"</b>
  con eso podras acceder a tu maquina a la base de datos que tiene el docker compose en esta version fue eliminada ya que ese puerto estaba en uso.
  
2. Si despues de ejecutar el docker compose el servidor no levanta solo ejecuta d nuevo docker start <nombrecontenedor> ya que el codigo no esta preparado para esperar el contendor de la base de datos este listo, con la tabla necesaria,
Se puede arreglar pero ya es de codigo python.

3. La red aunque se llama mi_red docker agrega el prefijo del nombre de la imagen por ejemplo <b>miproyect_mi_red</b>
