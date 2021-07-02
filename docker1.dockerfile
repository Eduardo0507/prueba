FROM alpine
ENV Hoy = Viernes
RUN echo "Comando de imagen"
CMD echo "Comando de inicialización $Hoy"
###END DOCKERFILE###