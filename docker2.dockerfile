####DOCKERFILE####
FROM alpine

ENV HOY=viernes

RUN echo "Comando de imagen"

CMD echo "Comando de Incializacion $HOY"
###END DOCKERFILE###